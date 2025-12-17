from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Booking, BookingStatusHistory
from apps.services.models import StylistService

class BookingService:
    @transaction.atomic
    def create_booking(self, customer, service, stylist, time_slot, notes=''):
        if time_slot.is_booked:
            raise ValidationError("Time slot is already booked.")
            
        # Calculate price
        price = service.price
        # Check for custom price
        try:
            stylist_service = StylistService.objects.get(stylist=stylist, service=service)
            if stylist_service.custom_price:
                price = stylist_service.custom_price
        except StylistService.DoesNotExist:
            pass # Use base price
            
        booking = Booking.objects.create(
            customer=customer,
            stylist=stylist,
            service=service,
            time_slot=time_slot,
            status='pending',
            notes=notes,
            total_price=price
        )
        
        # Mark slot as booked
        time_slot.is_booked = True
        time_slot.save()
        
        # Create history
        BookingStatusHistory.objects.create(
            booking=booking,
            status='pending',
            notes='Booking created'
        )
        
        return booking
