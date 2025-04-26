from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.jpg")

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to="book_covers/", null=True, blank=True)

    def __str__(self):
        return self.title
