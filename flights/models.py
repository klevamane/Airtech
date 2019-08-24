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


def validate_airport_code(value):
    if len(value) != 3:
        raise ValidationError('The airport code must be of 3 characters')

    if not value.isalpha():
        raise ValidationError('airport code should contain only letters')


class Airport (AbstractBaseModel):
    """Airport"""
    code = models.CharField(max_length=3, null=False, blank=False, validators=[validate_airport_code], unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return '{} airport in {}'.format(self.code, self.city)


class Flight(AbstractBaseModel):
    """The Flight model class"""

    name = models.CharField(max_length=40, null=False, blank=False)
    code = models.CharField(max_length=6, null=False, blank=False)
    source = models.ForeignKey(Airport, related_name='flights', on_delete=models.DO_NOTHING)
    destination = models.ForeignKey(Airport, related_name='destinations', on_delete=models.DO_NOTHING)
    takeoff_time = models.DateTimeField(null=False, blank=False)
    arrival_time = models.DateTimeField(null=False, blank=False)
    gate = models.IntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    seats = models.IntegerField(validators=[validate_seats], null=False, blank=False,)
    status = models.CharField(max_length=10, validators=[validate_status], default='active')

    def __str__(self):
        return 'flight name {} flight code {}'.format(self.name, self.code)

    # Todo get the total number of available seats

    @property
    def bookable_seats(self):
        return self.seats - self.tickets.count()
    # Todo validate that source and destination is not the same
