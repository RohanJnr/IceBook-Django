from django.db import connection

from rest_framework import serializers

from .models import Post
from icebook.apps.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    num_likes = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    num_comments = serializers.SerializerMethodField(read_only=True)
    has_liked = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "user",
            "title",
            "likes",
            "num_likes",
            "comments",
            "num_comments",
            "description",
            "created",
            "has_liked"
        ]
        read_only_fields = ('created')


    def get_likes(self, obj):
        return [liked_user.profile.username for liked_user in obj.likes.all()]

    def get_num_likes(self, obj):
        return obj.likes.count()

    def get_comments(self, obj):
        request = self.context.get("request")
        comments_dict = {}

        for com in obj.comment_set.all():
            user_profile = com.user.profile

            if user_profile.username in comments_dict:
                comments_dict[user_profile.username]["comments"][com.comment] = com.commented_time

            else:
                comments_dict[user_profile.username] = {
                    "profile_pic": user_profile.get_profile_picture_url(request),
                    "comments": {
                        com.comment: com.commented_time
                    }
                }

        return comments_dict


    def get_num_comments(self, obj):
        return obj.comment_set.count()

    def get_has_liked(self, obj):
        has_liked = False
        request = self.context.get("request")
        if request:
            user = request.user
            has_liked = user in obj.likes.all()
        return has_liked
