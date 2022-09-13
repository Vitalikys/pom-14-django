#створення image
# pull official base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apt-get -y install libpq-dev gcc && pip install psycopg2

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt
# copy project to .    in root folder our files
COPY . .