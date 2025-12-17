from django.db import models
from apps.core.models import TimeStampedModel

class Salon(TimeStampedModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='salon/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class OperatingHours(TimeStampedModel):
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='operating_hours')
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_closed = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('salon', 'day_of_week')
        ordering = ['day_of_week']
    
    def __str__(self):
        return f"{self.get_day_of_week_display()}: {self.opening_time} - {self.closing_time}"

class Holiday(TimeStampedModel):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='holidays')
    name = models.CharField(max_length=100)
    date = models.DateField()
    is_recurring = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} ({self.date})"
