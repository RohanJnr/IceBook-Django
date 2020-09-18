from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Post, Comment
from icebook.apps.users.serializers import UserSerializer


class PostSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    num_likes = SerializerMethodField()
    num_comments = SerializerMethodField()
    has_liked = SerializerMethodField()
    has_control = SerializerMethodField()

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
            "has_liked",
            "has_control",
            "archived",
        )
        read_only_fields = ("user", "num_likes", "num_comments", "has_liked", "created")

    @staticmethod
    def get_num_likes(obj: Post) -> int:
        """Get Number of Likes."""
        return obj.likes.count()

    @staticmethod
    def get_num_comments(obj: Post) -> int:
        """Get Number of comments."""
        return obj.comment_set.count()

    def get_has_liked(self, obj: Post) -> bool:
        """Check if current authenticated user has liked the Post."""
        has_liked = False
        request = self.context.get("request")
        if request:
            user = request.user
            has_liked = user in obj.likes.all()
        return has_liked

    def get_has_control(self, obj: Post) -> bool:
        """Check if current authenticated user is the author of the Post."""
        request = self.context.get("request")
        if request.user == obj.user:
            return True
        return False


class CommentSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "commented_time", "comment")
        read_only_fields = ("commented_time",)
