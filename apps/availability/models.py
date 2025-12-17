from django.db import models
from apps.core.models import TimeStampedModel
from apps.accounts.models import Stylist

class Availability(TimeStampedModel):
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, related_name='availabilities')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Availabilities'
        ordering = ['date', 'start_time']
        
    def __str__(self):
        return f"{self.stylist} - {self.date} ({self.start_time}-{self.end_time})"

class TimeSlot(TimeStampedModel):
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, related_name='time_slots')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['date', 'start_time']
        unique_together = ('stylist', 'date', 'start_time')
        
    def __str__(self):
        return f"{self.stylist} - {self.date} {self.start_time}"
