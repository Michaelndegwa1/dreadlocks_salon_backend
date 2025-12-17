from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryViewSet, ServiceViewSet, StylistServiceViewSet

router = DefaultRouter()
router.register(r'categories', ServiceCategoryViewSet)
router.register(r'list', ServiceViewSet)
router.register(r'stylist-services', StylistServiceViewSet, basename='stylist-services')

urlpatterns = [
    path('', include(router.urls)),
]
