from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalonViewSet, OperatingHoursViewSet, HolidayViewSet, StylistViewSet

router = DefaultRouter()
router.register(r'info', SalonViewSet)
router.register(r'hours', OperatingHoursViewSet)
router.register(r'holidays', HolidayViewSet)
router.register(r'stylists', StylistViewSet, basename='stylist')

urlpatterns = [
    path('', include(router.urls)),
]
