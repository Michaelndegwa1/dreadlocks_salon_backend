from rest_framework import viewsets, permissions
from apps.accounts.models import Stylist
from apps.accounts.serializers import StylistSerializer
from .models import Salon, OperatingHours, Holiday
from .serializers import SalonSerializer, OperatingHoursSerializer, HolidaySerializer

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class OperatingHoursViewSet(viewsets.ModelViewSet):
    queryset = OperatingHours.objects.all()
from rest_framework import viewsets, permissions
from apps.accounts.models import Stylist
from apps.accounts.serializers import StylistSerializer
from .models import Salon, OperatingHours, Holiday
from .serializers import SalonSerializer, OperatingHoursSerializer, HolidaySerializer

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class OperatingHoursViewSet(viewsets.ModelViewSet):
    queryset = OperatingHours.objects.all()
    serializer_class = OperatingHoursSerializer
    permission_classes = [permissions.IsAdminUser]

class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StylistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer
    permission_classes = [permissions.AllowAny]
