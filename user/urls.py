from django.urls import path, include
from user.views import ListUsers

urlpatterns = [
    path('', ListUsers.as_view(), name='list_user')
]
