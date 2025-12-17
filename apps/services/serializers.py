from rest_framework import serializers
from .models import ServiceCategory, Service, StylistService

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Service
        fields = '__all__'

class StylistServiceSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)
    service_description = serializers.CharField(source='service.description', read_only=True)
    
    class Meta:
        model = StylistService
        fields = '__all__'
