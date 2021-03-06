from django.urls import path

from . import views


app_name = "users"

urlpatterns = [
    path("", views.HomeLoginView.as_view(), name="home"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("create-profile", views.CreateProfileView.as_view(), name="create-profile"),
    path("profile/<str:username>", views.ProfileView.as_view(), name="profile"),
    path("profile/edit", views.ProfileEditView.as_view(), name="edit-profile"),
]
