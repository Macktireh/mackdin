release: python3 manage.py collectstatic --no-input && python manage.py migrate
web: gunicorn config.wsgi --log-file -