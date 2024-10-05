# Gateway service

The Gateway service is an API designed to interface with different services and store results in a database, providing basic CRUD functionality.



## Description

**Key Dependencies:**
- Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs.
- DRF-YASG: Yet Another Swagger Generator for Django REST framework.

## Running the Service

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Access the Swagger documentation at [http://localhost:8000/](http://localhost:8000/) to explore and test the API.


## Getting Started (First-Time Setup)

Install dependencies
```bash
pip install -r requirements.txt
```

Follow these simple steps to set up the Django application and database for the first time:

1. **Make Migrations:**
    Run the following command to create migration files:
    ```bash
    python manage.py makemigrations
    ```

2. **Migrate:**
    Apply the migrations to set up the database schema:
    ```bash
    python manage.py migrate
    ```

3. **Create Superuser:**
    Create an administrative user to manage the Django admin interface:
    ```bash
    python manage.py createsuperuser
    ```

4. **Run Django Server:**
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

5. **Explore the API:**
    Access the API and explore its functionalities using the Swagger interface:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Basic Django Commands

Run the Django server:
```bash
python manage.py runserver
```
View the API via Django admin:
http://127.0.0.1:8000/admin/

Access the Swagger interface:
http://127.0.0.1:8000/

Rebuilding Django models:
```bash
python manage.py makemigrations
python manage.py migrate
```
create a new app
```bash
django-admin startapp api
```
Creating a superuser (Remember to use a secure username and password, especially in production):
```bash
python manage.py createsuperuser
```


# Running the project in docker

todo finish docker compose build
