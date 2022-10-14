#створення image
# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
#RUN apt-get -y install libpq-dev gcc && pip install psycopg2-binary

# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .

RUN pip install -r req.txt
# copy project to .    in root folder our files
COPY . .