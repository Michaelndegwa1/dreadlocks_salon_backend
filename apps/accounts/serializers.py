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
    role = serializers.ChoiceField(choices=['customer', 'stylist', 'manager'], write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_number', 'role')

    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        
        user = User(**validated_data)
        user.set_password(password)
        
        if role == 'customer':
            user.is_customer = True
        elif role == 'stylist':
            user.is_stylist = True
        elif role == 'manager':
            user.is_manager = True
            
        user.save()
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
