from rest_framework import generics, status
from rest_framework.response import Response

from .serializer import UserSerializer
from .models import User
# Create your views here.


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.object.all().exclude(is_admin=True)
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

    queryset = User.object.all().exclude()
    serializer_class = UserSerializer

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
    queryset = User.object.all()
    serializer_class = UserSerializer
