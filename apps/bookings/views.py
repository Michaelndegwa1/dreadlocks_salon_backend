from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'service', 'stylist', 'customer']
    search_fields = ['id', 'customer__user__first_name', 'customer__user__last_name', 'customer__user__email', 'service__name']
    ordering_fields = ['created_at', 'time_slot__date']
    ordering = ['-created_at']
    
    def get_queryset(self):
        user = self.request.user
        queryset = Booking.objects.all()
        
        if user.is_customer:
            queryset = queryset.filter(customer__user=user)
        elif user.is_stylist:
            queryset = queryset.filter(stylist__user=user)
        # Managers see all
            
        return queryset
        
    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        return BookingSerializer
