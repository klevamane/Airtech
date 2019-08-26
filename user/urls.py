from django.urls import path, include
from user.views import ListCreateUsers, UpdateUser, RetrieveUser, UserPassport

urlpatterns = [
    path('', ListCreateUsers.as_view(), name='list_user'),
    path('update/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/', RetrieveUser.as_view(), name='retrieve_user'),
    path('delete/<int:pk>/', UserPassport.as_view(), name='delete_user_passport')
]
