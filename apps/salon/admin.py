from django.contrib import admin
from .models import Salon, OperatingHours, Holiday

class OperatingHoursInline(admin.TabularInline):
    model = OperatingHours
    extra = 7

class HolidayInline(admin.TabularInline):
    model = Holiday
    extra = 1

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    inlines = [OperatingHoursInline, HolidayInline]

admin.site.register(OperatingHours)
admin.site.register(Holiday)
