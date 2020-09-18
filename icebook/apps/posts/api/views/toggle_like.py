from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from icebook.apps.posts.models import Post


class ToggleLike(APIView):
    """Like a un-liked post and vice versa."""

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request: Request, id: int) -> Response:
        response = {}
        user = request.user
        post = Post.objects.get(id=id)
        if user in post.likes.all():
            post.likes.remove(user)
            response["has_liked"] = False
        else:
            post.likes.add(user)
            response["has_liked"] = True

        return Response(response)
