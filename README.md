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
$ chmod +x entrypoint.sh
$ docker-compose up -d --build
```

If local changes won't update in the container, try the followings:

```
$ docker-compose stop
$ docker system prune --volumes
$ docker-compose up -d --build
```

heroku:

check: http://flask-tdd.herokuapp.com/users, http://flask-tdd.herokuapp.com/ping

```
$ heroku create flask-tdd
$ heroku login
$ heroku addons:create heroku-postgresql:hobby-dev --app flask-tdd
$ docker build -f Dockerfile.prod -t registry.heroku.com/flask-tdd/web .
$ heroku config:get DATABASE_URL --app flask-tdd
postgres://vlooduhjgnbnqz:34f9549c24f1f30040953b1953b0f37897e73c1396160d12212c17431d8807ee@ec2-35-174-88-65.compute-1.amazonaws.com:5432/d66i6mdu7av344
$ export DATABASE_URL=postgres://vlooduhjgnbnqz:34f9549c24f1f30040953b1953b0f37897e73c1396160d12212c17431d8807ee@ec2-35-174-88-65.compute-1.amazonaws.com:5432/d66i6mdu7av344
$ docker run --name flask-tdd -e "PORT=8765" -p 5002:8765 registry.heroku.com/flask-tdd/web:latest
$ docker rm flask-tdd
$ docker push registry.heroku.com/flask-tdd/web:latest
$ heroku container:release web --app flask-tdd
$ heroku run python manage.py recreate_db --app flask-tdd
$ heroku run python manage.py seed_db --app flask-tdd
$ brew install httpie
$ http --json POST https://flask-tdd.herokuapp.com/users username=hello email=hello@world.com
```

Test Coverage:

```
$ docker-compose up -d --build
$ docker-compose exec users pytest "project/tests" -p no:warnings --cov="project"
$ docker-compose exec users pytest "project/tests" -p no:warnings --cov="project" --cov-report="html"
```

Flake8 (linting), Black(formatting), isort (sorting)

```
$ docker-compose up -d --build
$ docker-compose exec users flake8 project
$ docker-compose exec users black project --check
$ docker-compose exec users black project --diff
$ docker-compose exec users black project
$ docker-compose exec users /bin/sh -c "isort project/*/*.py --check-only"
$ docker-compose exec users /bin/sh -c "isort project/*/*.py --diff"
$ docker-compose exec users /bin/sh -c "isort project/*/*.py"
$ docker-compose exec users flake8 project
$ docker-compose exec users black project --check
$ docker-compose exec users /bin/sh -c "isort project/*/*.py --check-only"
```
