from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Availability, TimeSlot
from .serializers import AvailabilitySerializer, TimeSlotSerializer
from .services import AvailabilityService
from apps.accounts.models import Stylist
from datetime import datetime

class AvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if hasattr(self.request.user, 'is_stylist') and self.request.user.is_stylist:
            return Availability.objects.filter(stylist__user=self.request.user)
        return Availability.objects.none()

class TimeSlotViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TimeSlotSerializer
    permission_classes = [permissions.AllowAny]
    queryset = TimeSlot.objects.all()
    
    def get_queryset(self):
        queryset = TimeSlot.objects.all()
        stylist_id = self.request.query_params.get('stylist_id')
        date_str = self.request.query_params.get('date')
        
        if stylist_id:
            queryset = queryset.filter(stylist_id=stylist_id)
        if date_str:
            queryset = queryset.filter(date=date_str)
            
        return queryset

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def generate(self, request):
        stylist_id = request.data.get('stylist_id')
        date_str = request.data.get('date')
        
        if not stylist_id or not date_str:
            return Response({'error': 'stylist_id and date are required'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            stylist = Stylist.objects.get(id=stylist_id)
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            service = AvailabilityService()
            service.generate_time_slots(stylist, target_date)
            
            return Response({'status': 'generated'})
        except Stylist.DoesNotExist:
            return Response({'error': 'Stylist not found'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)
