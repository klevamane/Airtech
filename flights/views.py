from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from helpers.utils import set_true_context

from .models import Airport, Flight
from .serializers import AirportSerializer, FlightSerializer


class ListFlights(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    # Todo list of available flight should be
    # flights with take of time greater than now
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FlightSerializer(queryset, many=True)
        context = set_true_context(serializer.data, "operation successful")
        return Response(data=context, status=status.HTTP_200_OK)


class CreateFlight(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    permission_classes = [IsAdminUser]


class UpdateFlight(generics.UpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminUser]


class DeleteFlight(generics.DestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminUser]


class RetrieveFlight(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        context = set_true_context(serializer.data, "operation successful")
        return Response(context, status=status.HTTP_200_OK)


class AddAirport(generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AirportSerializer(queryset, many=True)
        context = set_true_context(serializer.data, "operation successful")
        return Response(context, status=status.HTTP_200_OK)
