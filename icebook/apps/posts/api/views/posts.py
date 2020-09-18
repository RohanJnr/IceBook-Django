from django.db.models.query import QuerySet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from icebook.apps.posts.models import Post
from icebook.apps.posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """TODO: docs"""

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.get_posts(False)
    serializer_class = PostSerializer
    lookup_field = "id"

    def get_serializer_context(self) -> dict:
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer: PostSerializer) -> None:
        serializer.save(user=self.request.user)

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        username = self.request.query_params.get("username", None)
        if username is not None:
            return queryset.filter(user__profile__username=username)
        return queryset
