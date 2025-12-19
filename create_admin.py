import os
import django
import sys

print("Starting Admin Creation Script...")
sys.stdout.flush()

# Use the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

try:
    django.setup()
    print("Django setup successful")
    sys.stdout.flush()
except Exception as e:
    print(f"Django setup failed: {e}")
    sys.stdout.flush()
    sys.exit(1)

from apps.accounts.models import User

email = "admin@uptown.com"
password = "Admin123!"

try:
    if not User.objects.filter(email=email).exists():
        User.objects.create_superuser(email=email, password=password)
        print(f"Successfully created superuser: {email}")
    else:
        user = User.objects.get(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f"Updated existing superuser: {email}")
    sys.stdout.flush()
except Exception as e:
    print(f"Operation failed: {e}")
    sys.stdout.flush()
    sys.exit(1)
