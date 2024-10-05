FROM python:3.8-slim

WORKDIR /app

RUN pip install --upgrade pip


COPY . /app

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate



