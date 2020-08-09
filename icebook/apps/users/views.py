from django.shortcuts import render
from django.views import View


class RegisterView(View):
    """User registration page (displayed in the home page)."""
    pass


class LoginView(View):
    """User login page (displayed in the home page)."""
    pass


class ProfileView(View):
    """Profile of logged-in User."""
    pass


class ProfileUpdateView(View):
    """Update User profile data."""
    pass


class DeleteUserView(View):
    """Delete User."""
    pass
    

