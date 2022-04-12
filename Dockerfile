FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc 
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .
COPY ./database/init.sql/ /docker-entrypoint-initdb.d/create_tables.sql


RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]