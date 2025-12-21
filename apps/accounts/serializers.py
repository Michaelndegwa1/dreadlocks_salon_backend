from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer, Stylist, Manager

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'profile_image', 'is_customer', 'is_stylist', 'is_manager')
        read_only_fields = ('is_customer', 'is_stylist', 'is_manager')

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True, default='customer')
    specialties = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_number', 'role', 'specialties')

    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        specialties = validated_data.pop('specialties', [])
        
        user = User(**validated_data)
        user.set_password(password)
        
        if role == 'customer':
            user.is_customer = True
        elif role == 'stylist':
            user.is_stylist = True
        elif role == 'manager':
            user.is_manager = True
            
        user.save()

        # Handle specialties for stylists
        if role == 'stylist' and specialties:
            # The signal creates the profile, so we just need to update it
            # We refresh from db to ensure we have the profile created by signal
            user.refresh_from_db()
            if hasattr(user, 'stylist_profile'):
                user.stylist_profile.specialties = specialties
                user.stylist_profile.save()

        return user

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'

class StylistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Stylist
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Manager
        fields = '__all__'
