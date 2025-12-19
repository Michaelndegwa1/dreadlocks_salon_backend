from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all().order_by('-created_at')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'payment_method']
    search_fields = ['transaction_id', 'booking__customer__user__first_name', 'booking__customer__user__last_name', 'booking__customer__user__email']
    ordering_fields = ['created_at', 'amount']
    
    def get_queryset(self):
        user = self.request.user
        if user.is_customer:
            return Payment.objects.filter(booking__customer__user=user)
        elif user.is_stylist:
            return Payment.objects.filter(booking__stylist__user=user)
        elif user.is_manager:
            return Payment.objects.all()
        return Payment.objects.none()
