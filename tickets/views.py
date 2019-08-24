from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from .serializers import TicketSerializer
from .models import Tickets


class CreateTicket(generics.CreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # update flight seat


