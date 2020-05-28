from django.contrib import admin

# Register your models here.
from .models import Flight,Airport,Passenger

class PassengerInline(admin.StackedInline):
  model=Passenger.flights.through
  extra=1

class FlightAdmin(admin.ModelAdmin):
    inlines=[PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
