from django.urls import path, include

from . import views


app_name = "posts"

urlpatterns = [
    path("", include("icebook.apps.posts.api.urls")),
    path("posts/", views.ListPosts.as_view(), name="list-posts"),
    path("add-post/", views.AddPost.as_view(), name="add-post"),
    path("posts/<int:pk>", views.DetailPost.as_view(), name="detail-post"),
]
