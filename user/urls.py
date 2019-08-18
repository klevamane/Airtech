from django.urls import path, include
from user.views import ListCreateUsers

urlpatterns = [
    path('', ListCreateUsers.as_view(), name='list_user')
]
