from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login']
        read_only_fields = ('id', 'is_admin', 'last_login', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RetrieveUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login']
        read_only_fields = ('id', 'is_admin', 'last_login', 'is_active')


class UpdateUserSerializer (ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'is_admin', 'is_active', 'email', 'created_at', 'updated_at', 'last_login')
        exclude = ['is_admin', 'last_login', 'is_active']
