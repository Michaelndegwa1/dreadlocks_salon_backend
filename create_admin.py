#!/usr/bin/env python
"""
Quick script to create an admin superuser account.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create superuser
email = 'mike@gmail.com'
password = 'admin123'  # Change this to your desired password
first_name = 'Mike'
last_name = 'Admin'

try:
    # Check if user exists
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        print(f"✅ Updated existing user '{email}' to superuser!")
    else:
        # Create new superuser
        user = User.objects.create_superuser(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        print(f"✅ Created new superuser '{email}'!")
    
    print(f"\nLogin credentials:")
    print(f"   Email: {email}")
    print(f"   Password: {password}")
    print(f"\n⚠️  Remember to change the password after first login!")
    
except Exception as e:
    print(f"❌ Error: {e}")


