from django.urls import path, include
from .views import CreateTicket

urlpatterns = [
    path('reservation/', CreateTicket.as_view(), name='create_ticket')
]
