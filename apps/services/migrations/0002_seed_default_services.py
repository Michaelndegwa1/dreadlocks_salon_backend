from django.db import migrations

def seed_defaults(apps, schema_editor):
    # This migration is now empty to avoid conflicts with 0003_seed_correct_services.py
    pass


def remove_defaults(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_defaults, remove_defaults),
    ]
