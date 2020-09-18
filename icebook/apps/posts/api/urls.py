from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    path(
        "api/toggle-like/<int:id>", views.ToggleLike.as_view(), name="toggle-like-api"
    ),
    path("api/comment", views.CommentView.as_view(), name="add-comment-api"),
    path("api/", include(router.urls)),
]
