from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from icebook.apps.users.forms import ProfileCreationForm
from icebook.apps.users.models import Profile


class CreateProfileView(LoginRequiredMixin, View):
    """Setup User profile after the registration process."""

    template_name = "users/create-profile.html"

    def get(self, request):
        """Render profile creation form."""
        if request.user.has_profile():
            return redirect("users:profile")
        print("hello")
        profile_form = ProfileCreationForm()
        context = {"profile_form": profile_form}
        return render(request, self.template_name, context)

    def post(self, request):
        """Validate profile creation form and save."""
        profile_form = ProfileCreationForm(request.POST, request.FILES)
        if profile_form.is_valid():
            user = request.user
            obj = profile_form.save(commit=False)
            obj.user = user
            obj.save()
            username = profile_form.cleaned_data["username"]
            return redirect("users:profile", username=username)

        context = {"profile_form": profile_form}
        return render(request, self.template_name, context)


class ProfileView(LoginRequiredMixin, View):
    """Profile of logged-in User."""

    template_name = "users/profile.html"

    def get(self, request, username):
        """Render User profile."""

        # adding prefetch and select related on 1 instance isn't going to help.
        # TODO: research
        user_profile = (
            Profile.objects.select_related("user")
            .prefetch_related(
                "user__post_set", "user__post_set__comment_set", "user__post_set__likes"
            )
            .get(username=username)
        )

        context = {
            "user_profile": user_profile,
            "user_posts": user_profile.user.post_set.all()
            }
        return render(request, self.template_name, context)


class ProfileEditView(LoginRequiredMixin, View):
    """Update User profile data."""

    template_name = "users/edit-profile.html"

    def get(self, request):
        """Render profile form with User data."""
        user_profile = request.user.profile
        profile_form = ProfileCreationForm(instance=user_profile)
        context = {"profile_form": profile_form}
        return render(request, self.template_name, context)

    def post(self, request):
        """Update profile of User."""
        user_profile = request.user.profile
        profile_form = ProfileCreationForm(
            request.POST, request.FILES, instance=user_profile
        )
        if profile_form.is_valid():
            profile_form.save()
            return redirect("users:profile")

        context = {"profile_form": profile_form}
        return render(request, self.template_name, context)
