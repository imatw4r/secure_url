#!/bin/bash
echo "Starting application"
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); u = User.objects.get_or_create(username='${ADMIN_USER}')[0]; u.email='${ADMIN_EMAIL}'; u.set_password('${ADMIN_PASSWORD}'); u.save()" | python manage.py shell
gunicorn secure_url.wsgi --bind :8000 --chdir=/app
