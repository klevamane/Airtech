from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('is_admin', 'last_login', 'is_active')

    def create(self, validated_data):
        return User.object.create_user(**validated_data)
