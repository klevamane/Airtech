from django.urls import path, include
from .views import ListFlights, RetrieveFlight, UpdateFlight, CreateFlight, AddAirport

urlpatterns = [
    path('all/', ListFlights.as_view(), name='list_flights'),
    path('detail/<int:pk>/', RetrieveFlight.as_view(), name='flight_detail'),
    path('update/<int:pk>/', UpdateFlight.as_view(), name='update_flight'),
    path('add/flight/', CreateFlight.as_view(), name='add_flight'),
    path('add/airport/', AddAirport.as_view(), name="add_airport")

]
