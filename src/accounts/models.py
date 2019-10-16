from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="profile_pics", default="default.png")
	bio = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"{self.user}'s profile"

	def save(self):
	    super().save()

	    img = Image.open(self.image.path)

	    if img.height > 300 or img.width > 300:
	        output_size = (420, 420)
	        img.thumbnail(output_size)
	        img.save(self.image.path)
