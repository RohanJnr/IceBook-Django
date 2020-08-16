from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username"
        ]
    
    def get_username(self, obj):
        return obj.profile.username