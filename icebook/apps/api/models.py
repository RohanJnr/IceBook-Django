from django.db import models


class Message(models.Model):
    author = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.message}"
