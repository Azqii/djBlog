#!/bin/sh

python3 manage.py migrate

gunicorn --bind 0.0.0.0:8000 djBlog.wsgi