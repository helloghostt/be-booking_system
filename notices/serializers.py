from rest_framework import serializers
from .models import Notice
from accounts.serializers import UserSerializer

class NoticeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Notice
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'author')