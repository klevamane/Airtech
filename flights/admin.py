from django.contrib import admin
from flights.models import Flight
# Register your models here.


@admin.register(Flight)
class FlightsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'code', 'source', 'destination', 'status', 'takeoff_time')
    list_display_links = ('id', 'code')
    search_fields = ('code', 'source', 'name')
