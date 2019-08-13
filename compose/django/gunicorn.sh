#!/bin/bash

python3 /yuejian3/manage.py collectstatic --noinput --settings=yuejian3.settings.prod &&
python3 /yuejian3/manage.py makemigrations --settings=yuejian3.settings.prod &&
python3 /yuejian3/manage.py migrate --settings=yuejian3.settings.prod

gunicorn -c /gunicorn.py yuejian3.wsgi

