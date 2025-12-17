from django.db import models
from apps.core.models import TimeStampedModel
from apps.accounts.models import Customer, Stylist
from apps.services.models import Service
from apps.availability.models import TimeSlot

class Booking(TimeStampedModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    time_slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE, related_name='booking')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Booking {self.id} - {self.customer} with {self.stylist}"

class BookingStatusHistory(TimeStampedModel):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='status_history')
    status = models.CharField(max_length=20, choices=Booking.STATUS_CHOICES)
    changed_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.booking} - {self.status}"
