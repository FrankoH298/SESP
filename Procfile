web: gunicorn core.wsgi
release: python manage.py makemigrations && python manage.py migrate
web: daphne core.asgi:application --port $PORT --bind 0.0.0.0