from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("api/posts", views.ListPosts.as_view(), name="list-posts-api"),
    path("api/posts/<int:pk>", views.DetailPost.as_view(), name="detail-post-api")
]

urlpatterns = format_suffix_patterns(urlpatterns)