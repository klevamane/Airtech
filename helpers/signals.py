from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework import status

from tickets.models import Tickets
from flights.models import Flight


