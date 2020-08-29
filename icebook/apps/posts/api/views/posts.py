from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from icebook.apps.posts.models import Post
from icebook.apps.posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """TODO: docs"""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.get_posts()
    serializer_class = PostSerializer
    lookup_field = "id"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
