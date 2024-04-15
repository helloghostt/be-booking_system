from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    court = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'court', 'start_time', 'end_time', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)