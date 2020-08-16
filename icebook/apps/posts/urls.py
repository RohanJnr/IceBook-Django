from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = "posts"

urlpatterns = [
    path("", include("icebook.apps.posts.api.urls")),
    path("posts/", TemplateView.as_view(template_name="posts/list-posts.html"), name="list-posts"),
    path("new-post", views.NewPost.as_view(), name="new-post")
]

# urlpatterns = [
#     path("add-post/", views.add_post_view, name="add-post"),
#     path("posts/", views.display_posts_view, name="display-posts"),
#     path("posts/<int:pk>", views.detail_post_view, name="detail-post"),
#     path("posts/<int:pk>/add-comment", views.comments_view, name="add-comment"),
#     path("posts/<int:pk>/add-like/<str:destination>", views.like_view, name="like"),
#     path("posts/<int:pk>/delete-post", views.delete_post_view, name="delete-post"),
#     path("posts/<int:pk>/update-post", views.update_post_view, name="update-post"),
#     path("posts/<int:pk>/archive", views.archive_post_view, name="archive"),
#     path("posts/<int:pk>/un-archive", views.unarchive_post_view, name="un-archive")
# ]
