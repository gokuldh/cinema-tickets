# CinemaSeat Backend/Frontend

This is a simple Django project that lets you book seat with only one seat per user.

## Requirement
```
Django= 2.1.5
python-dotenv= 0.10.1
```

## How to install

Just clone it from here. and run following command
```
(On linux)
cp .env.example .env

(on Windows)
copy .env.example .env
```
fill all the environment variables in the .env file.

```
python manage.py migrate

python manage.py runserver

```

## Environment variables

For development: Using sqlite you can use other Engines as well. Make sure to install better Database engine for production.

```
SECRET_KEY=<yourKey>
DEBUG=True|False
ENGINE=django.db.backends.mysql,
NAME=<Db_name>,
USER=<Db_user>,
PASSWORD=<Db_password>,
HOST=<Db_host>,
PORT=<Db_port>
```
## Access Backend

First create a superuser

```

python manage.py createsuperuser --username=<username> --email=<emailaddr>

```
then run server and append /admin after your ip.

## Seats creation

There are 5 fields in the backend
```
seat_no: required | unique | not null
row_no: required | not null | (used to make row of seats)
seat_name: required | (used to differentiate from numeric seat row combination like: A1,A2,B1,B2 etc. )
booked_by: (left it empty because it will be filled by user later on)
ip: required | not null | (fill random value and it will be updated when user book a ticket by its ip)

```

## Special Instructions

Do not push your .env file on git and keep it safe with you for production deployment because it contains your secret key and db info.
