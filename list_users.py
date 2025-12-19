#!/usr/bin/env python
"""
List all users in the database who can login.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

print("=" * 70)
print("ALL USERS WHO CAN LOGIN")
print("=" * 70)

users = User.objects.all().order_by('email')

if not users.exists():
    print("\nNo users found in database.")
else:
    print(f"\nTotal users: {users.count()}\n")
    print(f"{'Email':<40} {'Active':<8} {'Staff':<8} {'Superuser':<10} {'Name'}")
    print("-" * 70)
    
    for user in users:
        active = "Yes" if user.is_active else "No"
        staff = "Yes" if user.is_staff else "No"
        superuser = "Yes" if user.is_superuser else "No"
        name = f"{user.first_name} {user.last_name}".strip() or "N/A"
        
        print(f"{user.email:<40} {active:<8} {staff:<8} {superuser:<10} {name}")

print("\n" + "=" * 70)
print("NOTES:")
print("=" * 70)
print("- Users with 'Active: Yes' can login")
print("- Users with 'Staff: Yes' can access admin portal")
print("- Users with 'Superuser: Yes' have full admin privileges")
print("=" * 70)

