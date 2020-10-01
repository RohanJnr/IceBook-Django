# IceBook-Django
This is a social media website built using django.

# Want to contribute?
- Email me at: rohanjnr44@gmail.com
- Or contact me on discord: Iceman#6508

# Setup Guide

### requirements
- python3.7 or higher
- pipenv 
  - Get it by running **pip install pipenv**

### Setup Guide
##### 1.Cloning the repo
- Clone the repo or fork it and then clone from your profile.
- Cd into **IceBook-Django**
- Create a new branch by doing the following:
  - **git checkout -b branch_name**
##### 2.Pipenv and migrations
- Go to directory where the pipfile is and run **pipenv sync --dev**
- Activate pipenv by doing **pipenv shell**
- Go into the src folder where the manage.py sits and run the following:
  - **python manage.py makemigrations**
  - **python manage.py migrate**
  
##### 3.Super user and Profile
- Create super user by doing the following:
  - **python manage.py createsuperuser**
  - You need to manually create a profile for your user(this will be automated in the future.).
  
##### 4.Env vars
- Go the the folder **icebook** where the settings.py file sits and create a file called **.env**
- Add the following inside the file:
  - ```SECRET_KEY = 'secret_key_here' ```
  
##### 5.Running the server
- Go the folder where your manage.py sits and the following commands to run the server:
  - **python manage.py runserver**
  or
  - **pipenv run start**

##### 6. Compile SCSS to CSS
- Requires Node.js. Install -> https://nodejs.org/en/
- cd into **icebook/frontend/** folder.
- Run **npm run sass_compile** to compile all SCSS to CSS.
- If you want to edit the SCSS, run **npm run sass** to enable watch feature.
