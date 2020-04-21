from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ["bio", "image", "website"]

class SearchForm(forms.Form):
	name = forms.CharField(label="Username", max_length=120)
