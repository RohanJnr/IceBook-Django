from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from icebook.apps.users.forms import ProfileCreationForm
from icebook.apps.posts.models import Post


class CreateProfileView(LoginRequiredMixin, View):
    """Setup User profile after the registration process."""

    template_name = "users/create-profile.html"


    def get(self, request):
        """Render profile creation form."""
        if request.user.has_profile():
            return redirect("users:profile")

        profile_form = ProfileCreationForm()
        context = {
            "profile_form": profile_form
        }
        return redirect(request, self.template_name, context)
    
    def post(self, request):
        """Validate profile creation form and save."""
        profile_form = ProfileCreationForm(request.POST, request.FILES)
        if profile_form.is_valid():
            user = request.user

            obj = profile_form.save(commit=False)
            obj.user = user
            obj.save()

            return redirect("users:profile")
        
        context = {
            "profile_form": profile_form
        }
        return redirect(request, self.template_name, context)


class ProfileView(LoginRequiredMixin, View):
    """Profile of logged-in User."""

    template_name = "users/profile.html"

    def get(self, request):
        """Render User profile."""
        user_posts = Post.objects.filter(user=request.user).select_related("user")
        
        context = {
            "user_posts": user_posts
        }
        return render(request, self.template_name,   context)


class ProfileEditView(LoginRequiredMixin, View):
    """Update User profile data."""

    template_name = "users/edit-profile.html"

    def get(self, request):
        """Render profile form with User data."""
        user_profile = request.user.profile
        profile_form = ProfileCreationForm(instance=user_profile)
        context = {
            "profile_form": profile_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """Update profile of User."""
        user_profile = request.user.profile
        profile_form = ProfileCreationForm(
                request.POST,
                request.FILES,
                instance=user_profile
            )
        if profile_form.is_valid():
            profile_form.save()
            return redirect("users:profile")
        
        context = {
            "profile_form": profile_form
        }
        return render(request, self.template_name, context)
