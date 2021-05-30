from django.utils.dateparse import parse_date
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from flights.models import Flight
from helpers.serialization_message import FAILURE_MSG, SUCCESS_MSG
from helpers.utils import set_false_context, set_true_context, validate_date

from .models import Tickets
from .serializers import TicketSerializer


class CreateTicket(generics.CreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        flight_id = kwargs.get("flight_id")
        try:
            flight = Flight.objects.get(pk=flight_id)

        except Flight.DoesNotExist:
            context = set_false_context(
                None, FAILURE_MSG["does_not_exist"].format("flight")
            )
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

        if flight.bookable_seats < 1:
            context = set_false_context(None, FAILURE_MSG["all_seats_booked"])
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

        data = {"flight_id": kwargs.get("flight_id"), "customer": request.user.id}
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            context = set_true_context(
                serializer.data, SUCCESS_MSG["successful_reservation"]
            )
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetReservations(generics.ListAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer

    def list(self, request, *args, **kwargs):
        is_valid_date = validate_date(self.request.GET.get("date"))
        if not is_valid_date and is_valid_date is not None:
            context_error = {"message": FAILURE_MSG["incorrect_date_format"]}
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
        date_str = self.request.GET.get("date")
        if date_str:
            date = parse_date(date_str)
            reservations = Tickets.objects.filter(
                payment_status="reserved", created_at=date
            )
        else:
            reservations = Tickets.objects.filter(payment_status="reserved").all()
        serializer = TicketSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
