from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("add-post/", views.add_post_view, name="add-post"),
    path("posts/", views.display_posts_view, name="display-posts"),
    path("posts/<int:pk>", views.detail_post_view, name="detail-post"),
    path("posts/<int:pk>/add-comment", views.comments_view, name="add-comment"),
    path("posts/<int:pk>/add-like/<str:destination>", views.like_view, name="like"),
    path("posts/<int:pk>/delete-post", views.delete_post_view, name="delete-post"),
    path("posts/<int:pk>/update-post", views.update_post_view, name="update-post"),
    path("posts/<int:pk>/archive", views.archive_post_view, name="archive"),
    path("posts/<int:pk>/un-archive", views.unarchive_post_view, name="un-archive")
]
