import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

try:
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@uptownlocs.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
except Exception as e:
    print(f"Error in create_admin.py: {e}")
