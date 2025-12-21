web: /bin/bash -c "python manage.py collectstatic --noinput || true && python manage.py migrate && python create_admin.py || true && gunicorn config.wsgi --log-file -"
