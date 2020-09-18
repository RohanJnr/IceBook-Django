from django.contrib.auth import authenticate, login
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


from icebook.apps.users.forms import CustomUserLoginForm


class HomeLoginView(View):
    """
    Home Page for base URI: '/'.

    Users will be able to login from the home page.
    """

    template_name = "users/home.html"

    def get(self, request: WSGIRequest) -> HttpResponse:
        # Redirect to posts page when already logged in.
        if request.user.is_authenticated:
            return redirect("posts:list-posts")

        # Render landing page when user is not logged in.
        login_form = CustomUserLoginForm()
        context = {"login_form": login_form}
        return render(request, self.template_name, context)

    def post(self, request: WSGIRequest) -> HttpResponse:
        """Handle user authentication."""
        login_form = CustomUserLoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data["email"]
            password = login_form.cleaned_data["password"]

            user = authenticate(email=email, password=password)
            login(request, user)

            return redirect("posts:list-posts")

        context = {"login_form": login_form}
        return render(request, self.template_name, context)
