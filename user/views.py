from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import UserSerializer, RetrieveUserSerializer, UpdateUserSerializer
from .models import User
from helpers.utils import IsOwner, IsOwnerOrIsAdmin
# Create your views here.


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all().exclude(is_admin=True)
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        context = {
            'data': serializer.data,
            'message': 'operation successful',
            'success': True
        }

        return Response(context, status=status.HTTP_200_OK)


class RetrieveUser(generics.RetrieveAPIView):
    """Get the iser detail"""

    queryset = User.objects.all().exclude()
    serializer_class = RetrieveUserSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrIsAdmin)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        context = {
            'data': serializer.data,
            'message': 'operation successful',
            'success': True
        }
        return Response(context, status=status.HTTP_200_OK)


class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsAuthenticated, IsOwner)
