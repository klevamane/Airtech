from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import FlightSerializer
from .models import Flight

from helpers.utils import I


class ListFlight(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


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
