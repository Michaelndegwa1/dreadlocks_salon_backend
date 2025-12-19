from rest_framework import serializers
from .models import Booking
from apps.services.models import Service
from apps.accounts.models import Stylist
from apps.availability.models import TimeSlot
from .services import BookingService

from apps.accounts.serializers import CustomerSerializer, StylistSerializer

class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    stylist = StylistSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'
        depth = 1

class BookingCreateSerializer(serializers.Serializer):
    service_id = serializers.IntegerField()
    stylist_id = serializers.IntegerField()
    time_slot_id = serializers.IntegerField()
    notes = serializers.CharField(required=False, allow_blank=True)
    
    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_customer:
             raise serializers.ValidationError("Only customers can create bookings.")
             
        customer = user.customer_profile
        service = Service.objects.get(id=validated_data['service_id'])
        stylist = Stylist.objects.get(id=validated_data['stylist_id'])
        time_slot = TimeSlot.objects.get(id=validated_data['time_slot_id'])
        
        booking_service = BookingService()
        return booking_service.create_booking(
            customer=customer,
            service=service,
            stylist=stylist,
            time_slot=time_slot,
            notes=validated_data.get('notes', '')
        )
