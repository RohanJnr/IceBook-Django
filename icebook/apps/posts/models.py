from django.conf import settings
from django.db import models
from django.db.models import Count
from django.db.models.signals import post_delete

from .signals import delete_pic

from PIL import Image


USER_MODEL = settings.AUTH_USER_MODEL


class PostManager(models.Manager):

	def get_posts(self, status: bool = False):
		return self.get_queryset().select_related("user", "user__profile").prefetch_related("likes__profile", "comments__user__profile").filter(archived=status)

class Post(models.Model):
	user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	description = models.TextField()
	likes = models.ManyToManyField(USER_MODEL, related_name="likes", blank=True)
	comments = models.ManyToManyField(
		"Comment",
		related_name="comments",
		blank=True
		)
	archived = models.BooleanField(default=False)

	objects = PostManager()

	def __str__(self):
		return f"{self.user} : {self.title}"

	class Meta:
		ordering = ['-created']


class Comment(models.Model):
	user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
	commented_time = models.DateTimeField(auto_now_add=True, auto_now=False)
	comment = models.CharField(max_length=250)


post_delete.connect(delete_pic, Post)