from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Customer, Stylist, Manager

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_customer and not hasattr(instance, 'customer_profile'):
            Customer.objects.create(user=instance)
        elif instance.is_stylist and not hasattr(instance, 'stylist_profile'):
            Stylist.objects.create(user=instance)
        elif instance.is_manager and not hasattr(instance, 'manager_profile'):
            Manager.objects.create(user=instance)
