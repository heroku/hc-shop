#!/bin/sh

python manage.py createdb --noinput --nodata
python manage.py collectstatic --noinput
