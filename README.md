# BigUps

BigUps is a project created after the website Awaards. The app enables users to login or signup and see projects posted by other users, post their own projects and rate projects. Users can also view their profile, update them and get to view the API created by this project.

## Behavior Driven Development

- Users can view posted projects and their details
- Users can post a project to be rated/reviewed by others
- Users can rate/review projects
- Users can search for projects
- Authenticated users can view and update their profile

## Getting started

To get a copy of the project up and running on your local machine for development and testing purposes;

1. Clone the repository

   > git clone https://github.com/Wannjer1/big-ups.git

2. Create a virtual environment

   > virtual3 -m venv venv

   > source venv/bin/activate

3. Install the project dependencies

   > (venv) $ pip install -r requirements.txt

4. Create a postgress db
5. Apply all migrations

   > (venv) $ python manage.py migrate

6. Create admin account

   > (venv) $ python manage.py createsuperuser

7. Make migrations to your database

   > (venv) $ python manage.py makemigrations (appname)

   > (venv) $ python manage.py migrate

8. Start development server
   > (venv) $ python3 manage.py runserver

## Running Tests

Run automated tests for this system

> (venv) $ python3 manage.py test (appname)

## Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to Heroku to see it live.

## Built with

- Django 4.0.1-web framework
- Python3.9- backend logic
- PostgreSQL- database system
- Heroku- deployment platform

## Author

Ann Wanjeri

## License

MIT License
