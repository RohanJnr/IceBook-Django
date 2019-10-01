# IceBook-Django

This is a social media website built using django.

# Setup Guide

### requirements

- python3.7 or higher
- pipenv
  - Get it by running **pip install pipenv**

### Setep Guide

##### 1.Cloning the repo

- Clone the repo or fork it and then clone from your profile.
- Then Type **cd IceBook-Django**
- Create a new branch by doing the following:
  - **git checkout -b branch_name**

##### 2.Pipenv and migrations

- Go to directory where the pipfile is and run **pipenv shell**
- Go into the src folder where the manage.py sits and run the following:

  - **python manage.py makemigrations**
  - **python manage.py migrate**

##### 3.Super user

- Create super user by doing the following:

  - **python manage.py createsuperuser**

##### 4.Env vars

- Go the the folder **icebook** where the settings.py file sits and create a file called **.env**
- Add the following inside the file:

  - `SECRET_KEY = 'secret_key_here'`

##### 5.Running the server

- Go the folder where your manage.py sits and the following commands to run the server:
  - **python manage.py runserver**
