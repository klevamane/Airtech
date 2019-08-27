from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes


from django.http import Http404, HttpResponseForbidden

from .serializer import UserSerializer, RetrieveUserSerializer, UpdateUserSerializer
from .models import User
from helpers.utils import IsOwner, IsOwnerOrIsAdmin
# Create your views here.


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all().exclude(is_admin=True)
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden()
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        context = {
            'data': serializer.data,
            'message': 'operation successful',
            'success': True
        }

        return Response(context, status=status.HTTP_200_OK)


class RetrieveUser(generics.RetrieveAPIView):
    """Get the user detail"""

    queryset = User.objects.all()
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
    parser_classes = (MultiPartParser,)
    serializer_class = UpdateUserSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop ('partial', False)
        instance = self.get_object ()
        serializer = self.get_serializer (instance, data=request.data, partial=partial)
        serializer.is_valid (raise_exception=True)

        serializer.save ()

        return Response (serializer.data)


class UserPassport(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    def get_single_user_object(self, pk):
        try:
            return User.objects.get (pk=pk)
        except User.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        if request.user.id != pk:
            return HttpResponseForbidden()
        user_photo_to_be_deleted = self.get_single_user_object(pk=pk)
        user_photo_to_be_deleted['image'] = None
        user_photo_to_be_deleted.save()
        return Response (status=status.HTTP_200_OK)

    # permission_classes = (IsAuthenticated, IsOwner)
