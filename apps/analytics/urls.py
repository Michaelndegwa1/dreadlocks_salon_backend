from django.urls import path
from .views import DashboardStatsView, AnalyticsReportsView

urlpatterns = [
    path('dashboard-stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('reports/', AnalyticsReportsView.as_view(), name='analytics-reports'),
]
