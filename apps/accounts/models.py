from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel
from .managers import CustomUserManager

class User(AbstractUser, TimeStampedModel):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    is_customer = models.BooleanField(default=False)
    is_stylist = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Customer(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    
    def __str__(self):
        return f"Customer: {self.user.email}"

class Stylist(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='stylist_profile')
    bio = models.TextField(blank=True)
    specialties = models.JSONField(default=list, blank=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Stylist: {self.user.email}"

class Manager(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager_profile')
    
    def __str__(self):
        return f"Manager: {self.user.email}"
