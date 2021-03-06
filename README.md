# Django Site

## Packages

### Global Environment

- Python 3.7.3
- Virtualenv 16.6.0
- pylint
- autopep8
- flake8

### Virtual Environment

- Django 2.2.2
- pillow
- django-crispy-forms

## commands

- Start project

```shell
django-admin startprojects config .
```



- Run server

```shell
python manage.py runserver <ip:port>
``` 

- Migration

```shell
python manage.py makemigration
python manage.py migrate
```

- Create superuser

```shell
python manage.py createsuperuser
<username>
<email>
<password>
<confirm password> 
```

- Create a New app

```shell
python manage.py startapp core
```