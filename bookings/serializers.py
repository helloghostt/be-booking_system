from rest_framework import serializers
from .models import Booking
from accounts.serializers import UserSerializer
from courts.serializers import CourtSerializer

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    court = CourtSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'user', 'court', 'start_time', 'end_time', 'created_at')