#!/usr/bin/env bash
echo "------flask init-----"
flask db init
echo "------flask migrate-----"
flask db migrate
echo "------flask upgrade-----"
flask db upgrade
# flask run --host=0.0.0.0
echo "------gunicorn-----"
gunicorn -b 0.0.0.0:5000 run:app