from rest_framework import viewsets, permissions
from .models import ServiceCategory, Service, StylistService
from .serializers import ServiceCategorySerializer, ServiceSerializer, StylistServiceSerializer

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class StylistServiceViewSet(viewsets.ModelViewSet):
    serializer_class = StylistServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if hasattr(self.request.user, 'is_stylist') and self.request.user.is_stylist:
            return StylistService.objects.filter(stylist__user=self.request.user)
        return StylistService.objects.all()
