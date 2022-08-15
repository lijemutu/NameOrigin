FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc build-essential
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .
COPY ./database/init.sql/ /docker-entrypoint-initdb.d/create_tables.sql

CMD flask db init
CMD flask db migrate
CMD flask db upgrade
CMD gunicorn -b 0.0.0.0:5000 run:app


# RUN chmod u+x ./entrypoint.sh
# ENTRYPOINT ["./entrypoint.sh"]