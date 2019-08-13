from rest_framework import generics

from .serializer import UserSerializer
from .models import User
# Create your views here.


class ListUsers(generics.ListCreateAPIView):
    queryset = User.object.all().exclude()
    serializer_class = UserSerializer
