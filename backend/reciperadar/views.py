from django.shortcuts import render
from rest_framework import viewsets
from reciperadar.models import UserProfile, Recipe, SavedRecipe, Review
from reciperadar.serializers import UserSerializer, RecipeSerializer, SavedRecipeserializer, ReviewSearializers
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset= UserProfile.objects.all()
    serializer_class= UserSerializer
    
class RecipeViewSet(viewsets.ModelViewSet):
    queryset= Recipe.objects.all()
    serializer_class= RecipeSerializer
    
class SavedRecipeViewSet(viewsets.ModelViewSet):
    queryset= SavedRecipe.objects.all()
    serializer_class= SavedRecipeserializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.objects.all()
    serializer_class= ReviewSearializers