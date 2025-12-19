import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()

from apps.services.models import ServiceCategory

categories = ['Maintenance', 'Starters', 'Styling']

for cat_name in categories:
    category, created = ServiceCategory.objects.get_or_create(name=cat_name)
    if created:
        print(f'Created category: {cat_name}')
    else:
        print(f'Category already exists: {cat_name}')
