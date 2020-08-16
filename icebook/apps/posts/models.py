from django.conf import settings
from django.db import models
from django.db.models import Count
from django.db.models.signals import post_delete

from .signals import delete_pic

from PIL import Image


USER_MODEL = settings.AUTH_USER_MODEL

class PostManager(models.Manager):

	def get_posts(self, status: bool = False):
		return self.get_queryset().prefetch_related("likes").prefetch_related("comments").filter(archived=status)

class Post(models.Model):
	user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	img = models.ImageField(upload_to="post_imgs", blank=True, null=True)
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
		
	def save(self):
		super().save()
		if self.img:
			img = Image.open(self.img.path)

			if img.height > 300 or img.width > 300:
				output_size = (600, 600)
				img.thumbnail(output_size)
				img.save(self.img.path)


class Comment(models.Model):
	user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
	commented_time = models.DateTimeField(auto_now_add=True, auto_now=False)
	comment = models.CharField(max_length=250)


post_delete.connect(delete_pic, Post)