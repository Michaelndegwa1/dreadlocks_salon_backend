#!/usr/bin/env python
"""
Script to check if a user exists and their status.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

email = 'mike@gmail.com'

print("=" * 60)
print("USER ACCOUNT CHECK")
print("=" * 60)

# Check if user exists
if User.objects.filter(email=email).exists():
    user = User.objects.get(email=email)
    print(f"\n✅ User '{email}' EXISTS")
    print(f"\nUser Details:")
    print(f"  - Email: {user.email}")
    print(f"  - First Name: {user.first_name}")
    print(f"  - Last Name: {user.last_name}")
    print(f"  - Is Active: {user.is_active}")
    print(f"  - Is Staff: {user.is_staff}")
    print(f"  - Is Superuser: {user.is_superuser}")
    print(f"  - Has Password: {bool(user.password)}")
    print(f"  - Date Joined: {user.date_joined}")
    print(f"  - Last Login: {user.last_login}")
    
    # Check password
    test_password = 'admin123'
    if user.check_password(test_password):
        print(f"\n✅ Password '{test_password}' is CORRECT")
    else:
        print(f"\n❌ Password '{test_password}' is INCORRECT")
        print(f"   Current password hash: {user.password[:50]}...")
    
    if not user.is_active:
        print(f"\n⚠️  WARNING: User is NOT ACTIVE - this will prevent login!")
    
else:
    print(f"\n❌ User '{email}' DOES NOT EXIST")
    print("\nCreating user now...")
    
    user = User.objects.create_user(
        email=email,
        password='admin123',
        first_name='Mike',
        last_name='User',
        is_active=True
    )
    print(f"✅ Created user '{email}' with password 'admin123'")

print("\n" + "=" * 60)

