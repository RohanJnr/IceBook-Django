from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("add-post/", views.add_post_view, name="add-post"),
    path("posts/", views.display_posts_view, name="display-posts"),
    path("posts/<str:slug>", views.detail_post_view, name="detail-post"),
    path("posts/<str:slug>/add-comment", views.comments_view, name="add-comment")
]
