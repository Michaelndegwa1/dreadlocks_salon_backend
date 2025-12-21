import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.services.models import Service, ServiceCategory

print(f'Categories: {ServiceCategory.objects.count()}')
for cat in ServiceCategory.objects.all():
    print(f' - {cat.name}')

print(f'Services: {Service.objects.count()}')
for svc in Service.objects.all():
    print(f' - {svc.name} ({svc.category.name})')
