from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register_view(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			create_profile(username)
			return redirect("login")

	else:
		form = RegisterForm()

	template_name = "accounts/register.html"
	context = {
	"form":form
	}
	return render(request, template_name, context)


def create_profile(username):
	user = User.objects.filter(username=username).first()
	user_profile = Profile()
	user_profile.user = user
	user_profile.save()


@login_required
def profile_view(request):
	template_name = "accounts/profile.html"
	context = {}
	return render(request, template_name, context)


@login_required
def update_view(request):
	if request.method == "POST":
		user_form = UserUpdateForm(request.POST, instance=request.user)

		profile_form = ProfileUpdateForm(
			request.POST,
			request.FILES,
			instance=request.user.profile
		)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect("profile")
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	template_name = "accounts/update.html"
	context = {
		"user_form":user_form,
		"profile_form":profile_form
	}
	return render(request, template_name, context)

@login_required
def delete_view(request):
	if request.method == "POST":
		username = request.user.username
		user = User.objects.get(username=username)
		user.delete()
		return redirect("register")
	template_name = "accounts/delete.html"
	context = {}
	return render(request, template_name, context)
