#!/bin/sh

python manage.py createdb --noinput
python manage.py collectstatic --noinput
