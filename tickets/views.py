from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.utils.dateparse import parse_date
from helpers.utils import IsOwnerOrIsAdmin

from datetime import datetime

from .serializers import TicketSerializer
from .models import Tickets
from flights.models import Flight
from helpers.utils import validate_date


class CreateTicket(generics.CreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            flight_id = kwargs.get("flight_id")
            flight = Flight.objects.get(pk=flight_id)

            if flight.bookable_seats < 1:
                context = {
                    "data": None,
                    "message": "The flight seats have all been booked",
                    "success": False,
                }
                return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
        except Flight.DoesNotExist:
            context = {
                "data": None,
                "message": "The flight does not exist",
                "success": False,
            }
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
        data = {"flight_id": kwargs.get("flight_id"), "customer": request.user.id}
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "data": serializer.data,
                "message": "Reservation made successfully, an email will be sent to you shortly",
                "success": True,
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetReservations(generics.ListAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer

    # def get_queryset(self):

    def list(self, request, *args, **kwargs):
        data = None
        is_valid_date = validate_date(self.request.GET.get('date'))
        if not is_valid_date and is_valid_date is not None:
            context_error = {"message": "Incorrect data format, should be YYYY-MM-DD"}
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
        date_str = self.request.GET.get('date')
        if date_str:
            date = parse_date(date_str)
            reservations = Tickets.objects.filter (payment_status="reserved", created_at=date)
            serializer = TicketSerializer (reservations, many=True)
        else:
            reservations = Tickets.objects.filter(payment_status="reserved").all()
            serializer = TicketSerializer(reservations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
