from django.db import models
from helpers.models import AbstractBaseModel
from django.core.exceptions import ValidationError
# Create your models here.

STATUS = ['landed', 'delayed', 'active', 'filled', 'airborne']

def validate_seats(value):
    if type(value) is not int:
        raise ValidationError('Must be an Integer')
    if value > 200:
        raise ValidationError('Total flight seats must not be more than 200')


def validate_status(value):
    if value not in STATUS:
        raise ValidationError('Wrong status')


class Flight(AbstractBaseModel):
    """The Flight model class"""

    name = models.CharField(max_length=40, null=False, blank=False)
    code = models.CharField(max_length=6, null=False, blank=False)
    source = models.CharField(max_length=100, null=False, blank=False)
    destination = models.CharField (max_length=100, null=False, blank=False)
    takeoff_time = models.DateTimeField(null=False, blank=False)
    arrival_time = models.DateTimeField(null=False, blank=False)
    gate = models.IntegerField(max_length=5, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    seats = models.PositiveIntegerField(default=0, null=False, blank=False, validators=[validate_seats])
    status = models.CharField(max_length=10, validators=[validate_status], default='active')

    def __str__(self):
        return 'flight name {} flight code {}'.format(self.name, self.code)

    # Todo get the total number of available seats



