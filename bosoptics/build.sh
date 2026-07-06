#!/usr/bin/env bash

set -o errexit

uv sync

python manage.py collectstatic --noinput

python manage.py migrate