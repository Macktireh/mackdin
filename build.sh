#!/usr/bin/env bash

set -o errexit  # exit on error

pip3 install -r requirements.txt --no-cache-dir
pip3 install --upgrade pip

python3 manage.py collectstatic --no-input
python3 manage.py migrate