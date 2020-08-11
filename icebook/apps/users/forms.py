from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta():
        model = CustomUser
        fields = ("first_name", "last_name", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email")


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid login credentials!!", "invalid")

class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            "bio": forms.Textarea(attrs={"cols": 80, "rows": 20}),
        }
