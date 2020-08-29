from rest_framework import status as s
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from icebook.apps.posts.models import Post
from icebook.apps.posts.serializers import CommentSerializer


class CommentView(APIView):
    """List all Posts."""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        post_id: str = request.query_params.get("post_id")

        if not post_id:
            error_dict: dict = {
                "Error": "post_id query parameter not given!"
            }
            return Response(error_dict, status=s.HTTP_400_BAD_REQUEST)

        post = Post.objects.prefetch_related("comment_set__user__profile").get(id=int(post_id))

        post_comments = post.comment_set.all()

        serializer = CommentSerializer(
            post_comments,
            many=True,
            context={"request": request}
        )

        return Response(serializer.data)

    @staticmethod
    def post(request):
        data = request.data.copy()
        data["post"] = int(data["post"])
        serializer = CommentSerializer(data=data, context={"request": request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=s.HTTP_201_CREATED)

        return Response(serializer.errors)
