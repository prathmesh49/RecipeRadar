from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=19, blank=True)
    password = models.CharField(max_length=19, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar_url = models.URLField(blank=True)
