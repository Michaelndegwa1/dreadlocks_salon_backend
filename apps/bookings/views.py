from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_customer:
            return Booking.objects.filter(customer__user=user)
        elif user.is_stylist:
            return Booking.objects.filter(stylist__user=user)
        elif user.is_manager:
            return Booking.objects.all()
        return Booking.objects.none()
        
    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        return BookingSerializer
