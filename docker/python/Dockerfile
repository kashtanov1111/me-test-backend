FROM python:3.9.16-alpine
LABEL 'MAINTAINER' = 'Oleg V. Ivantsov, email: o.v.ivantsov@gmail.com'

WORKDIR /var/www/html
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT gunicorn app.wsgi:application -w 2 -b :8000 --reload