from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	img = models.ImageField(upload_to="post_imgs", blank=True, null=True)
	description = models.TextField()
	slug = models.SlugField(unique=True)

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


class Likes(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	likes = models.PositiveIntegerField(default=0)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	commented_time = models.DateTimeField(auto_now_add=True, auto_now=False)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment = models.CharField(max_length=200)
