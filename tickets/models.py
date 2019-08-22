from django.db import models
from helpers.models import AbstractBaseModel
from django.apps import apps
from django.core.exceptions import ValidationError
from user.models import User

# Create your models here.

STATUS = ['reserved', 'paid']


def validate_payment_status(value):
    if value not in STATUS:
        raise ValidationError('Status must either be reserved or paid')


class Tickets(AbstractBaseModel):
    """The ticket class"""

    flight_id = models.ForeignKey('flight.flight', related_name='tickets', on_delete=models.DO_NOTHING)
    # enables User.tickets
    customer = models.ForeignKey('user.user', related_name='tickets', on_delete=models.DO_NOTHING)
    payment_status = models.CharField(max_length=8, validators=[validate_payment_status], default='reserved')
