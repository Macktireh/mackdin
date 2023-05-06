#!/usr/bin/env bash

set -o errexit  # exit on error

pip3 install --upgrade pip
pip3 install -r requirements.txt --no-cache-dir

python3 manage.py collectstatic --no-input
python3 manage.py migrate