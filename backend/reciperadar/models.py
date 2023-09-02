from django.utils import timezone
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=19, blank=True)
    password = models.CharField(max_length=19, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar_url = models.TextField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username+'--'+self.location
    


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.JSONField()
    instructions = models.TextField()
    cuisine = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.TextField(blank=True)
    UserProfile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title+'--'+self.cuisine
    
class SavedRecipe(models.Model):
    UserProfile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    
class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)