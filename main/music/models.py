from django.db import models
from django.contrib.auth.models import Permission, User


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=255)

