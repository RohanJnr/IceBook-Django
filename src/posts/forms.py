from django import forms
from .models import Post, Comment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class PostForm(forms.ModelForm):

	class Meta:
		model = Post

		fields = ["title", "description", "img"]


class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ["comment"]

	helper = FormHelper()