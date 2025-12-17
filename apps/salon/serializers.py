from rest_framework import serializers
from .models import Salon, OperatingHours, Holiday

class OperatingHoursSerializer(serializers.ModelSerializer):
    day_display = serializers.CharField(source='get_day_of_week_display', read_only=True)
    
    class Meta:
        model = OperatingHours
        fields = '__all__'

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'

class SalonSerializer(serializers.ModelSerializer):
    operating_hours = OperatingHoursSerializer(many=True, read_only=True)
    holidays = HolidaySerializer(many=True, read_only=True)
    
    class Meta:
        model = Salon
        fields = '__all__'
