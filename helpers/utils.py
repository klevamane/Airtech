from datetime import datetime

from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.response import Response


class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    # message = 'You must be the owner of this owner in order to make changes to the {}' \
    #     .format (obj.__class__.__name__)
    message = "You must be the owner in order to view or make changes"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method in SAFE_METHODS and obj.id == request.user.id:
            return True
        # Instance must have an attribute named `owner`. but ours is developer
        return obj == request.user


class IsOwnerOrIsAdmin(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    # message = 'You must be the owner of this owner in order to make changes to the {}' \
    #     .format (obj.__class__.__name__)
    message = "You must be the owner or an admin in order to view the users details"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method in SAFE_METHODS and obj.id == request.user.id:
            return True
        if request.method in SAFE_METHODS and request.user.is_admin:
            return True
        # Instance must have an attribute named `owner`. but ours is developer
        return obj == request.user


def get_context(message, data=None, outcome=True):
    return {"data": None, "message": "The flight does not exist", "success": False}


def send_light_email(subject, message, to):
    send_mail(
        subject,
        message,
        from_email="flight-reservations@airtech.com",
        recipient_list=[to],
        fail_silently=False,
    )


def validate_date(date_text):
    """Validate the date input

    Args:
        date_text(str): The date
    """
    if not date_text:
        return False
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def set_true_context(data, msg):
    return {"data": data, "message": msg, "success": True}


def set_false_context(data, msg):
    return {"data": data, "message": msg, "success": True}
