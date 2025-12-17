from datetime import datetime, timedelta, date
from .models import TimeSlot, Availability
from apps.salon.models import OperatingHours
from apps.accounts.models import Stylist

class AvailabilityService:
    def generate_time_slots(self, stylist, target_date):
        # Get operating hours for the day
        day_of_week = target_date.weekday()
        # Assuming only one salon for MVP or picking the first one
        # In real app, stylist belongs to a salon
        try:
            # This query assumes we can get operating hours. 
            # For MVP let's assume we fetch the first salon's hours or pass salon_id
            hours = OperatingHours.objects.filter(day_of_week=day_of_week).first()
        except OperatingHours.DoesNotExist:
            return [] 

        if not hours or hours.is_closed:
            return []

        slots = []
        current_time = datetime.combine(target_date, hours.opening_time)
        end_time = datetime.combine(target_date, hours.closing_time)
        
        while current_time + timedelta(minutes=30) <= end_time:
            slot_start = current_time.time()
            slot_end = (current_time + timedelta(minutes=30)).time()
            
            # Check if slot already exists
            if not TimeSlot.objects.filter(stylist=stylist, date=target_date, start_time=slot_start).exists():
                TimeSlot.objects.create(
                    stylist=stylist,
                    date=target_date,
                    start_time=slot_start,
                    end_time=slot_end,
                    is_booked=False
                )
            
            current_time += timedelta(minutes=30)
            
        return TimeSlot.objects.filter(stylist=stylist, date=target_date)
