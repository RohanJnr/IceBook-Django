from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from icebook.apps.users.forms import CustomUserCreationForm
from icebook.apps.users.mixins import NoLoginRequiredMixin


class RegisterView(NoLoginRequiredMixin, View):
    """User registration page."""

    template_name = "users/register.html"

    def get(self, request):
        """Render registration form."""
        registration_form = CustomUserCreationForm()
        context = {
            "registration_form": registration_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """Validate registration details, create account and authenticate."""
        registration_form = CustomUserCreationForm(request.POST)
        if registration_form.is_valid():
            # Check if email is valid - TODO
            email = registration_form.cleaned_data["email"]
            user = registration_form.save()
            login(request, user)
            return redirect("users:create-profile")
        
        context = {
            "registration_form": registration_form
        }
        return render(request, self.template_name, context)


class LogoutView(LoginRequiredMixin, View):
    """Log-out User."""

    def get(self, request):
        """Log-out User and redirect to home page."""
        logout(request)
        return redirect("users:home")


class DeleteUserView(LoginRequiredMixin, View):
    """Delete a User."""
    
    def get(self, request):
        """Delete User from database."""
        request.user.delete()
        return redirect("users:home")
