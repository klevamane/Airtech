from django.db import models
from helpers.models import AbstractBaseModel
from django.apps import apps
from django.core.exceptions import ValidationError
from user.models import User

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework import status

from flights.models import Flight
from helpers.utils import send_light_email

# Create your models here.

STATUS = ["reserved", "paid"]


def validate_payment_status(value):
    if value not in STATUS:
        raise ValidationError("Status must either be reserved or paid")


class Tickets(AbstractBaseModel):
    """The ticket class"""

    flight_id = models.ForeignKey(
        "flights.flight", related_name="tickets", on_delete=models.DO_NOTHING
    )
    # enables User.tickets
    customer = models.ForeignKey(
        "user.user", related_name="tickets", on_delete=models.DO_NOTHING
    )
    payment_status = models.CharField(
        max_length=8, validators=[validate_payment_status], default="reserved"
    )


@receiver(post_save, sender=Tickets)
def check_available_seat_exist(sender, instance, created, **kwargs):
    # send email here
    flight = Flight.objects.get(pk=instance.flight_id_id)
    payment_type = "Booking"
    if instance.payment_status == "reserved":
        payment_type = "Reservation"
    message = "Your ticket {} has been made successfully\n Flight Code:{}\n Departure: {}\n Arrival: {}\n Reservation date: {}\n Takeoff time: {}\n Arrival time: {}\n Reservation Id: {}".format(
        payment_type,
        flight.code,
        flight.source,
        flight.destination,
        instance.created_at,
        flight.takeoff_time,
        flight.arrival_time,
        instance.id,
    )
    send_light_email("Your flight ticket", message, "fogi@dot-mail.top")
