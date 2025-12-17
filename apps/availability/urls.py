from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AvailabilityViewSet, TimeSlotViewSet

router = DefaultRouter()
router.register(r'manage', AvailabilityViewSet, basename='availability')
router.register(r'slots', TimeSlotViewSet, basename='slots')

urlpatterns = [
    path('', include(router.urls)),
]
