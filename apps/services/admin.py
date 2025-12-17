from django.contrib import admin
from .models import ServiceCategory, Service, StylistService

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

admin.site.register(Service)
admin.site.register(StylistService)
