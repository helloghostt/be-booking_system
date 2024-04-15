from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Notice
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']