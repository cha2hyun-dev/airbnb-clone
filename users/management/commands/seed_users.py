import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
# from django_seed import Seed
from users.models import User
import random

__version__ = '0.1.9'


class Seed(object):
    instance = None
    seeders = {}
    fakers = {}

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Seed, cls).__new__(*args, **kwargs)
        return cls.instance

    def __init__(self):
        pass

    @staticmethod
    def codename(locale=None):
        from django.conf import settings
        locale = locale or getattr(settings, 'LANGUAGE_CODE', None)
        codename = locale or 'default'
        return codename

    @classmethod
    def faker(cls, locale=None, codename=None):
        code = codename or cls.codename(locale)
        if code not in cls.fakers:
            from faker import Faker
            cls.fakers[code] = Faker(locale)
            cls.fakers[code].seed_instance(random.randint(1, 10000))
        return cls.fakers[code]

    @classmethod
    def seeder(cls, locale=None):
        code = cls.codename(locale)
        if code not in cls.seeders:
            faker = cls.fakers.get(code, None) or cls.faker(codename=code)
            from django_seed import seeder
            cls.seeders[code] = seeder.Seeder(faker)

        return cls.seeders[code]


class Command(BaseCommand):

    help = "This command creates many user"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="How many users do you want to create")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
        users = User.objects.all()
        for user in users:
            if user.first_name == "Unnamed User":
                user.first_name = user.last_name
                user.save()
        self.stdout.write(self.style.SUCCESS(f"Done!"))
