#!/usr/bin/env python
"""
Script to create normal user accounts (not superusers) that can login to the admin portal.
These users don't need to be superusers - they just need to be active.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# List of users to create (you can modify this)
USERS_TO_CREATE = [
    {
        'email': 'admin@uptownlocs.com',
        'password': 'admin123',
        'first_name': 'Admin',
        'last_name': 'User',
        'is_staff': True,  # Allows access to admin panel
        'is_superuser': False  # Not a superuser, just staff
    },
    {
        'email': 'manager@uptownlocs.com',
        'password': 'manager123',
        'first_name': 'Manager',
        'last_name': 'User',
        'is_staff': True,
        'is_superuser': False
    },
    {
        'email': 'staff@uptownlocs.com',
        'password': 'staff123',
        'first_name': 'Staff',
        'last_name': 'Member',
        'is_staff': True,
        'is_superuser': False
    },
    {
        'email': 'mike@gmail.com',
        'password': 'admin123',
        'first_name': 'Mike',
        'last_name': 'User',
        'is_staff': True,  # Set to True to allow admin portal access
        'is_superuser': False
    }
]

def create_normal_users():
    print("=" * 60)
    print("CREATING NORMAL USER ACCOUNTS")
    print("=" * 60)
    print("\nThese users can login to the admin portal without being superusers.")
    print("They just need to be active and have is_staff=True for admin access.\n")
    
    created_users = []
    updated_users = []
    skipped_users = []
    
    for user_data in USERS_TO_CREATE:
        email = user_data['email']
        password = user_data['password']
        first_name = user_data.get('first_name', '')
        last_name = user_data.get('last_name', '')
        is_staff = user_data.get('is_staff', False)
        is_superuser = user_data.get('is_superuser', False)
        
        try:
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                # Update existing user
                user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = True
                user.is_staff = is_staff
                user.is_superuser = is_superuser
                user.save()
                updated_users.append((email, password))
                print(f"[OK] Updated: {email} (password: {password})")
            else:
                # Create new user
                user = User.objects.create_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    is_active=True,
                    is_staff=is_staff,
                    is_superuser=is_superuser
                )
                created_users.append((email, password))
                print(f"[OK] Created: {email} (password: {password})")
        except Exception as e:
            skipped_users.append((email, str(e)))
            print(f"[ERROR] Error with {email}: {e}")
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    if created_users:
        print(f"\n[OK] Created {len(created_users)} new user(s):")
        for email, password in created_users:
            print(f"   - {email} / {password}")
    
    if updated_users:
        print(f"\n[UPDATED] Updated {len(updated_users)} existing user(s):")
        for email, password in updated_users:
            print(f"   - {email} / {password}")
    
    if skipped_users:
        print(f"\n[ERROR] Skipped {len(skipped_users)} user(s):")
        for email, error in skipped_users:
            print(f"   - {email}: {error}")
    
    print("\n" + "=" * 60)
    print("LOGIN CREDENTIALS")
    print("=" * 60)
    print("\nYou can now login with any of these accounts:")
    all_users = created_users + updated_users
    for i, (email, password) in enumerate(all_users, 1):
        print(f"\n{i}. Email: {email}")
        print(f"   Password: {password}")
    
    print("\n[NOTE] These are normal users (not superusers) but can login to the admin portal.")
    print("       They have is_staff=True which allows admin access.")
    print("\n" + "=" * 60)

if __name__ == '__main__':
    create_normal_users()

