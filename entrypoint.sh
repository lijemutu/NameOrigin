#!/usr/bin/env bash
flask db init
flask db migrate
flask db upgrade
# flask run --host=0.0.0.0
gunicorn -b 127.0.0.1:5000 run:app