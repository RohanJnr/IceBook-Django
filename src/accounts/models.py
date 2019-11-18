from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save

from PIL import Image

from .signals import delete_profile_pic


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="profile_pics", default="default.png")
	bio = models.TextField(blank=True, null=True)
	website = models.URLField(max_length=300,null=True, blank=True)

	def __str__(self):
		return f"{self.user}'s profile"

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


# post_delete.connect(delete_profile_pic, Profile)
