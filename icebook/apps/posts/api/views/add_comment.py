from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from icebook.apps.posts.models import Post, Comment


class AddComment(APIView):
    """List all Posts."""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        comment = request.data["newComment"]
        post_id = request.data["postID"]
        comment_object = Comment(user=request.user, comment=comment)
        comment_object.save()
        post = Post.objects.get(id=post_id).comments.add(comment_object)

        res = {
            "user": request.user.profile.username,
            "comment": comment
        }

        return Response(res)
