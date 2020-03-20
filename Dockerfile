# pull official base image
FROM python:3.8.0-alpine

WORKDIR /usr/src/app

# PYTHONDONTWRITEBYTECODE Prevents Python from writing pyc files to disc
# PYTHONUNBUFFERED Prevents Python from buffering stdout and stderr 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD python manage.py run -h 0.0.0.0
