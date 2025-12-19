web: /bin/bash -c "python manage.py collectstatic --noinput && python manage.py migrate && python create_admin.py && gunicorn config.wsgi --log-file -"
