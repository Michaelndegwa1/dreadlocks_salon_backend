#!/usr/bin/env python
"""
Test the authentication endpoint directly to verify it works.
"""
import os
import django
import requests
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()

print("=" * 60)
print("TESTING AUTHENTICATION ENDPOINT")
print("=" * 60)

# Test data
email = 'mike@gmail.com'
password = 'admin123'

# Create test client
client = Client()

# Test the login endpoint
print(f"\n1. Testing login endpoint: POST /api/v1/auth/login/")
print(f"   Email: {email}")
print(f"   Password: {password}")

try:
    response = client.post(
        '/api/v1/auth/login/',
        data=json.dumps({'email': email, 'password': password}),
        content_type='application/json'
    )
    
    print(f"\n   Status Code: {response.status_code}")
    print(f"   Response: {response.content.decode()}")
    
    if response.status_code == 200:
        data = json.loads(response.content)
        if 'access' in data:
            print(f"\n✅ SUCCESS! Token received:")
            print(f"   Access token: {data['access'][:50]}...")
            if 'refresh' in data:
                print(f"   Refresh token: {data['refresh'][:50]}...")
        else:
            print(f"\n❌ ERROR: No access token in response")
            print(f"   Response data: {data}")
    else:
        print(f"\n❌ ERROR: Status code {response.status_code}")
        print(f"   Response: {response.content.decode()}")
        
except Exception as e:
    print(f"\n❌ EXCEPTION: {e}")
    import traceback
    traceback.print_exc()

# Also test with wrong password
print(f"\n2. Testing with wrong password (should fail):")
try:
    response = client.post(
        '/api/v1/auth/login/',
        data=json.dumps({'email': email, 'password': 'wrongpassword'}),
        content_type='application/json'
    )
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 401:
        print(f"   ✅ Correctly rejected wrong password")
    else:
        print(f"   ⚠️  Unexpected status code")
except Exception as e:
    print(f"   ❌ Exception: {e}")

print("\n" + "=" * 60)


