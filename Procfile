web: /bin/bash -c "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn config.wsgi --log-file -"
