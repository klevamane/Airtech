from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'is_admin', 'last_login', 'is_active')


class RetrieveUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login']
        read_only_fields = ('id', 'is_admin', 'last_login', 'is_active')


class UpdateUserSerializer (ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id', 'is_admin', 'is_active', 'email', 'created_at', 'updated_at', 'last_login')

    def create(self, validated_data):
        return User.object.create_user(**validated_data)
