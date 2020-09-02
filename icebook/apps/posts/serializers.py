from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Post, Comment
from icebook.apps.users.serializers import UserSerializer


class PostSerializer(ModelSerializer):
    user = UserSerializer()
    num_likes = SerializerMethodField()
    num_comments = SerializerMethodField()
    has_liked = SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "num_likes",
            "num_comments",
            "description",
            "image",
            "created",
            "has_liked"
        )
        read_only_fields = ("user", "num_likes", "num_comments", "has_liked", "created")

    @staticmethod
    def get_num_likes(obj):
        return obj.likes.count()

    @staticmethod
    def get_num_comments(obj):
        return obj.comment_set.count()

    def get_has_liked(self, obj):
        has_liked = False
        request = self.context.get("request")
        if request:
            user = request.user
            has_liked = user in obj.likes.all()
        return has_liked


class CommentSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "commented_time", "comment")
        read_only_fields = ("commented_time",)
