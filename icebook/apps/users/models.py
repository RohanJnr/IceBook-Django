from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete, post_save

from .signals import delete_profile_pic, resize_profile_pic


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The email is a required field.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


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
    GENDER_CHOICES = [(MALE, "Male"), (FEMALE, "Female"), (OTHER, "Other")]

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    username = models.CharField(
        max_length=128,
        help_text="Name for identity.",
        unique=True,
    )
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to="profile_pics", default="default.png")
    bio = models.CharField(max_length=256, blank=True)
    website = models.URLField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ["username"]

    def get_profile_picture_url(self, request):
        pic_url = self.profile_picture.url
        return request.build_absolute_uri(pic_url)

    def __str__(self):
        return f"{self.username}'s profile -> {self.user}"


post_save.connect(resize_profile_pic, sender=Profile)
post_delete.connect(delete_profile_pic, sender=Profile)
