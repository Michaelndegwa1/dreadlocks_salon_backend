from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegistrationView, UserProfileView, CustomerListView, StylistListView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('stylists/', StylistListView.as_view(), name='stylist-list'),
]
