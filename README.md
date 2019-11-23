# Airbnb Clone

```
Cloning Airbnb with Python, Django, Tailwind and more...
Last README update 19.11.22
```

# Installation

### pipenv

```bash
pipenv --three                  // python version 3
pipenv install django==2.2.6    // django version
pipenv shell                    // Enter a bubble
```

### Third Party App

```bash
pip install django-seed
pip install django-countries
pip install Pillow
pip install django-dotenv
pip install requests
```

### Initialize

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8080
```

### Seeding items

```bash
python manage.py seed_amenities
python manage.py seed_facilities
python manage.py seed_roomtypes
```

```bash
python manage.py seed_users --number 50
python manage.py seed_rooms --number 150
```

```bash
python manage.py seed_reviews --number 50
python manage.py seed_lists --number 50
python manage.py seed_reservations --number 50
```

### EMAIL

```bash
mailgun.com
ID : cha2hyun.dev@gmail.com
```

### Todo later

```bash
Beautify : verify_email.html
Fix : git login -> When user doesnt have any name, public email, bio 
```

### Tailwind Css Installation

```bash
0. install node.js
1. going to airbnb-clone folder
2. sudo apt install npm
3. npm init
4. npm install gulp gulp-postcss gulp-sass gulp-csso node-sass -D
5. npm install tailwindcss -D
6. sudo npm install -g npx
7. npx tailwind init
8. npm install autoprefixer -D
9. npm run css
```
