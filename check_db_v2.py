import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.services.models import Service, ServiceCategory

print(f'Categories: {ServiceCategory.objects.count()}')
sys.stdout.flush()
for cat in ServiceCategory.objects.all():
    print(f' - {cat.name}')
    sys.stdout.flush()

print(f'Services: {Service.objects.count()}')
sys.stdout.flush()
for svc in Service.objects.all():
    print(f' - {svc.name} ({svc.category.name})')
    sys.stdout.flush()
