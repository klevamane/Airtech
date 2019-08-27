release: python manage.py migrate --noinput
web: gunicorn app.wsgi:application --log-file - --log-level debug
