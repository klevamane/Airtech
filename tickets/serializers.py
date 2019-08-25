from rest_framework import serializers
from .models import Tickets


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ["id", "payment_status"]
        model = Tickets
        fields = "__all__"
