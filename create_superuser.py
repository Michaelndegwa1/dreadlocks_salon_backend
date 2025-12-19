#!/usr/bin/env python
"""
Script to create a Django superuser for UpTown Locs backend.
This script uses the custom User model that requires email instead of username.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    print("=" * 50)
    print("Creating Django Superuser")
    print("=" * 50)
    
    # Get user input
    email = input("Enter email address: ").strip()
    
    # Check if user already exists
    if User.objects.filter(email=email).exists():
        print(f"\n❌ User with email '{email}' already exists!")
        response = input("Do you want to make this user a superuser? (y/n): ").strip().lower()
        if response == 'y':
            user = User.objects.get(email=email)
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
            user.save()
            print(f"\n✅ User '{email}' is now a superuser!")
        return
    
    # Get password
    password = input("Enter password: ").strip()
    if not password:
        print("\n❌ Password cannot be empty!")
        return
    
    password_confirm = input("Confirm password: ").strip()
    if password != password_confirm:
        print("\n❌ Passwords do not match!")
        return
    
    # Get optional fields
    first_name = input("Enter first name (optional): ").strip()
    last_name = input("Enter last name (optional): ").strip()
    
    try:
        # Create superuser
        user = User.objects.create_superuser(
            email=email,
            password=password,
            first_name=first_name or '',
            last_name=last_name or ''
        )
        print(f"\n✅ Superuser '{email}' created successfully!")
        print(f"   You can now login to the admin panel at: /admin/")
    except Exception as e:
        print(f"\n❌ Error creating superuser: {e}")

if __name__ == '__main__':
    create_superuser()

