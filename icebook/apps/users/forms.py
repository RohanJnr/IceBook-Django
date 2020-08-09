from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta():
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class UserProfileCreationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ["user"]
        widgets = {
            "bio": Textarea(attrs={"cols": 80, "rows": 20}),
        }
