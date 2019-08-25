from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser

from .serializers import FlightSerializer, AirportSerializer
from .models import Flight
from .models import Airport


class ListFlights(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    #Todo list of available flight should be
    # flights with take of time greater than now
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FlightSerializer(queryset, many=True)
        context = {
            'data': serializer.data,
            'message': 'operation successful',
            'success': True
        }
        return Response(data=context, status=status.HTTP_200_OK)


class CreateFlight(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminUser]


class UpdateFlight(generics.UpdateAPIView):
    queryset = Flight.objects.all ()
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
        context = {
            'data': serializer.data,
            'message': 'operation successful',
            'success': True
        }
        return Response(context, status=status.HTTP_200_OK)


class AddAirport(generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AirportSerializer(queryset, many=True)
        context = {
            'data': serializer.data,
            'message': 'operation successful',
            'success': True
        }
        return Response(context, status=status.HTTP_200_OK)
