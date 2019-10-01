from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	img = models.ImageField(upload_to="post_imgs", blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return f"{self.user} : {self.title}"

	def save(self):
	    super().save()
	    if self.img:
		    img = Image.open(self.img.path)

		    if img.height > 300 or img.width > 300:
		        output_size = (400, 400)
		        img.thumbnail(output_size)
		        img.save(self.img.path)