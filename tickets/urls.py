from django.urls import path, include
from .views import CreateTicket, GetReservations

urlpatterns = [
    path("reservation/<int:flight_id>", CreateTicket.as_view(), name="create_ticket"),
    path("reservation/<int:flight_id>/all/", GetReservations.as_view(), name="get_reservations")
]
