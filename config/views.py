from django.http import JsonResponse
from django.shortcuts import redirect

def root_view(request):
    """Root view that redirects to API documentation"""
    return redirect('/api/schema/swagger-ui/')

def api_info(request):
    """API information endpoint"""
    return JsonResponse({
        'name': 'Dreadlocks Salon Booking API',
        'version': '1.0.0',
        'endpoints': {
            'authentication': '/api/v1/auth/',
            'services': '/api/v1/services/',
            'bookings': '/api/v1/bookings/',
            'salon': '/api/v1/salon/',
            'notifications': '/api/v1/notifications/',
            'documentation': '/api/schema/swagger-ui/',
        }
    })



