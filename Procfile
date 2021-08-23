release: python manage.py makemigrations && python manage.py migrate
web: daphne domecode.core.asgi --port 5000 --bind 0.0.0.0