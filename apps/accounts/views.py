from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer, UserSerializer, CustomerSerializer, StylistSerializer, ManagerSerializer

User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_serializer_class(self):
        user = self.request.user
        if not user.is_authenticated:
            return UserSerializer
        if hasattr(user, 'is_customer') and user.is_customer and hasattr(user, 'customer_profile'):
            return CustomerSerializer
        elif hasattr(user, 'is_stylist') and user.is_stylist and hasattr(user, 'stylist_profile'):
            return StylistSerializer
        elif hasattr(user, 'is_manager') and user.is_manager and hasattr(user, 'manager_profile'):
            return ManagerSerializer
        return UserSerializer

    def get_object(self):
        user = self.request.user
        if not user.is_authenticated:
            return user
        if hasattr(user, 'is_customer') and user.is_customer and hasattr(user, 'customer_profile'):
            return user.customer_profile
        elif hasattr(user, 'is_stylist') and user.is_stylist and hasattr(user, 'stylist_profile'):
            return user.stylist_profile
        elif hasattr(user, 'is_manager') and user.is_manager and hasattr(user, 'manager_profile'):
            return user.manager_profile
        return user
