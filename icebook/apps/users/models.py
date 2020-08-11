from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete, post_save

from .managers import CustomUserManager
from .signals import delete_profile_pic, resize_profile_pic


class CustomUser(AbstractUser):
    """User model for login credentials."""
    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_profile(self):
        """Check if the User has a profile."""
        return hasattr(self, "profile")

class Profile(models.Model):
    """Profile to display user public details."""
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    display_name = models.CharField(
            max_length=128,
            help_text="Name for identity.",
            unique=True,
        )
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(
            upload_to="profile_pics",
            default="default.png"
            )
    bio = models.CharField(max_length=512, blank=True)
    website = models.URLField(max_length=300,null=True, blank=True)

    class Meta:
        ordering = ["display_name"]

    def __str__(self):
        return f"{self.display_name}'s profile -> {self.user}"


post_save.connect(resize_profile_pic, sender=Profile)
post_delete.connect(delete_profile_pic, sender=Profile)
