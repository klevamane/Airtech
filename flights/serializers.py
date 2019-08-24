from rest_framework import serializers
from .models import Flight, Airport


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ['id']
        model = Flight
        fields = '__all__'

    def validate(self, data):
        """Check that the source and destination are not the same

        Args:
            self(obj): Instance
        """
        if data['source'] == data['destination']:
            # This shows as non_filed_errors
            raise serializers.ValidationError('The source and destination cannot be the same')

        if data['takeoff_time'] == data['arrival_time']:
            raise serializers.ValidationError('Departure and arrival time cannot be the same')

        if data['takeoff_time'] > data['arrival_time']:
            raise serializers.ValidationError('Departure time cannot be greater than arrival time')

        return data


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ['id']
        model = Airport
        fields = '__all__'
