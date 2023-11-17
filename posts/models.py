# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    