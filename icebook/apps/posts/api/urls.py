from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("api/posts", views.ListPosts.as_view(), name="list-posts-api"),
    path("api/posts/<int:id>", views.DetailPost.as_view(), name="detail-post-api"),
    path("api/toggle-like/<int:id>", views.ToggleLike.as_view(), name="toggle-like-api"),
    path("api/add-comment", views.AddComment.as_view(), name="add-comment-api")
]

urlpatterns = format_suffix_patterns(urlpatterns)