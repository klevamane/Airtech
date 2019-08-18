from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class IsOwner(BasePermission):
    """
       Object-level permission to only allow owners of an object to edit it.
       Assumes the model instance has an `owner` attribute.
    """
    # message = 'You must be the owner of this owner in order to make changes to the {}' \
    #     .format (obj.__class__.__name__)
    message = 'You must be the owner in order to view or make changes'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print('***** printing obj ', obj)
        print ('***** printing w222obj ', dir(obj))

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
    message = 'You must be the owner or an admin in order to view the users details'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print('***** printing obj ', obj)
        print ('***** printing w222obj ', dir(obj))

        if request.method in SAFE_METHODS and obj.id == request.user.id:
            return True
        if request.method in SAFE_METHODS and request.user.is_admin:
            return True
        # Instance must have an attribute named `owner`. but ours is developer
        return obj == request.user
