# flask-tdd-docker
code for tutorial at https://testdriven.io/courses/tdd-flask

# Setup

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=project/__init__.py
$ export FLASK_ENV=development
$ python manage.py run
```

# Docker

```
$ docker-compose build
$ docker-compose up -d
$ docker-compose stop
$ docker-compose up -d --build
$ docker-compose logs
```
