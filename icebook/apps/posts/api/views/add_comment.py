from rest_framework import status as s
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
        post = Post.objects.get(id=post_id)
        res = {}
        status = s.HTTP_201_CREATED

        try:
            comment_object = Comment(user=request.user, post=post, comment=comment)
            comment_object.save()
            res["user"] = {
                "username": request.user.profile.username,
                "profile_picture": request.user.profile.get_profile_picture_url(request)
                }
            res["comment_object"] = {
                "comment": comment_object.comment,
                "commented_time": comment_object.commented_time
                }

        except Exception as e:
            # TODO: add logging here.
            res["error"] = "Comment couldn't be added. Please try again later."
            status = s.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(res, status=status)
