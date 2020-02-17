from rest_framework import serializers
from .models import Message


class MessageSerialier(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'message', 'date_time']
