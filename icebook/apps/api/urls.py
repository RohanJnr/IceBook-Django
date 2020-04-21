from django.urls import path
from . import views


urlpatterns = [
    path("messages/", views.MessageList.as_view())
]
