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
            "profile_picture_url"
        ]
    
    def get_username(self, obj):
        return obj.profile.username

    def get_profile_picture_url(self, obj):
        request = self.context.get("request")
        pic_url = obj.profile.profile_picture.url
        return request.build_absolute_uri(pic_url)