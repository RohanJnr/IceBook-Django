from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "profile_picture_url",
        ]

    def get_username(self, obj: CustomUser) -> str:
        return obj.profile.username

    def get_profile_picture_url(self, obj: CustomUser) -> str:
        request = self.context.get("request")
        return obj.profile.get_profile_picture_url(request)
