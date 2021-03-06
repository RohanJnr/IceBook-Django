from django.conf import settings
from django.db import models
from django.db.models import Count
from django.db.models.signals import post_delete, post_save
from PIL import Image

from .signals import delete_post_image, resize_post_image


USER_MODEL = settings.AUTH_USER_MODEL


class PostManager(models.Manager):
    def get_posts(self, status: bool = False):
        return (
            self.get_queryset()
            .select_related("user", "user__profile")
            .prefetch_related("likes__profile", "comment_set__user__profile")
            .filter(archived=status)
        )


class Post(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    description = models.TextField()
    image = models.ImageField(upload_to="post_imgs")
    likes = models.ManyToManyField(USER_MODEL, related_name="likes", blank=True)
    archived = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return f"{self.user} : {self.description[:10]}"

    class Meta:
        ordering = ["-created"]


class Comment(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commented_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    comment = models.CharField(max_length=250)

    class Meta:
        ordering = ["-commented_time"]


post_delete.connect(delete_post_image, sender=Post)
post_save.connect(resize_post_image, sender=Post)
