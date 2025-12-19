#!/usr/bin/env python
"""
Script to create a regular user account for login.
This creates a normal user (not superuser) that can authenticate through the API.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_user():
    print("=" * 50)
    print("Creating Regular User Account")
    print("=" * 50)
    
    # Default user details - you can modify these
    email = 'mike@gmail.com'
    password = 'admin123'  # Change this to your desired password
    first_name = 'Mike'
    last_name = 'User'
    
    # Or get from input
    print("\nEnter user details (press Enter to use defaults):")
    email_input = input(f"Email [{email}]: ").strip()
    if email_input:
        email = email_input
    
    password_input = input(f"Password [{password}]: ").strip()
    if password_input:
        password = password_input
    
    first_name_input = input(f"First Name [{first_name}]: ").strip()
    if first_name_input:
        first_name = first_name_input
    
    last_name_input = input(f"Last Name [{last_name}]: ").strip()
    if last_name_input:
        last_name = last_name_input
    
    try:
        # Check if user exists
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print(f"\n⚠️  User '{email}' already exists!")
            response = input("Do you want to update this user? (y/n): ").strip().lower()
            if response == 'y':
                user.set_password(password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = True  # Ensure user is active
                user.save()
                print(f"✅ Updated user '{email}'!")
            else:
                print("❌ Cancelled.")
                return
        else:
            # Create new regular user
            user = User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_active=True  # Make sure user is active
            )
            print(f"✅ Created new user '{email}'!")
        
        print(f"\n{'='*50}")
        print("Login Credentials:")
        print(f"{'='*50}")
        print(f"Email:    {email}")
        print(f"Password: {password}")
        print(f"\n✅ This user can now login through the admin portal!")
        print(f"⚠️  Remember to change the password after first login!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    create_user()

