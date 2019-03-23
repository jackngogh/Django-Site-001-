# Django Site

## Packages

### Global Environment

- Python 3.7.2
- Virtualenv 6.4.3
- pylint
- autopep8
- flake8

### Virtual Environment

- Django 2.1.7
- pillow
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