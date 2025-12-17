from django.db import models
from apps.core.models import TimeStampedModel
from apps.accounts.models import Stylist

class ServiceCategory(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Service Categories'
        
    def __str__(self):
        return self.name

class Service(TimeStampedModel):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(help_text="Duration in minutes")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class StylistService(TimeStampedModel):
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, related_name='services')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='stylists')
    custom_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    custom_duration = models.PositiveIntegerField(blank=True, null=True, help_text="Custom duration in minutes")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('stylist', 'service')
        
    def __str__(self):
        return f"{self.stylist} - {self.service}"
