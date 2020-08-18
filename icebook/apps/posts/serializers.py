from django.db import connection

from rest_framework import serializers

from .models import Post
from icebook.apps.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    has_liked = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "likes",
            "comments",
            "title",
            "description",
            "created",
            "img",
            "has_liked"
        ]


    def get_likes(self, obj):
        return [liked_user.profile.username for liked_user in obj.likes.all()]

    def get_comments(self, obj):
        comments_dict = {}
        for com in obj.comments.all():
            comments_dict[com.user.profile.username] = com.comment
        return comments_dict

    def get_has_liked(self, obj):
        has_liked = False
        request = self.context.get("request")
        if request:
            user = request.user
            has_liked = user in obj.likes.all()
        return has_liked
