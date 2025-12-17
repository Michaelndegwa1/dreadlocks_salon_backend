from django.contrib import admin
from .models import Booking, BookingStatusHistory

class BookingStatusHistoryInline(admin.TabularInline):
    model = BookingStatusHistory
    readonly_fields = ('created_at', 'status', 'changed_by', 'notes')
    extra = 0

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'stylist', 'service', 'time_slot', 'status', 'total_price')
    list_filter = ('status', 'stylist', 'service')
    inlines = [BookingStatusHistoryInline]

admin.site.register(BookingStatusHistory)
