from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from reciperadar.models import UserProfile, Recipe, SavedRecipe, Review
from reciperadar.serializers import UserSerializer, RecipeSerializer, SavedRecipeserializer, ReviewSearializers
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset= UserProfile.objects.all()
    serializer_class= UserSerializer

    @action(methods=['get'], detail=False, url_path='username/(?P<username>\w+)')
    def getByUsername(self, request, username):
        user = get_object_or_404(UserProfile, username=username)
        data = UserSerializer(user, context={'request': request}).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecipeViewSet(viewsets.ModelViewSet):
    queryset= Recipe.objects.all()
    serializer_class= RecipeSerializer
    
class SavedRecipeViewSet(viewsets.ModelViewSet):
    queryset= SavedRecipe.objects.all()
    serializer_class= SavedRecipeserializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.objects.all()
    serializer_class= ReviewSearializers