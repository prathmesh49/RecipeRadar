from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
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
    
    @action(methods=['get'], detail=False, url_path='recipe/(?P<recipe>\w+)')
    def getByRecipe(self, request, recipe):
        # Filter reviews based on the specified recipe
        reviews = Review.objects.filter(recipe=recipe)
        
        # Serialize the queryset of reviews
        data = ReviewSearializers(reviews, many=True, context={'request': request}).data
        
        return Response(data, status=status.HTTP_200_OK)
    
@api_view(['GET'])  # Add this decorator
def searchRecipes(request):
    search_query = request.query_params.get('query', '')  # Get the search query from the request parameters

    if not search_query:
        return Response("Please provide a search query.", status=status.HTTP_400_BAD_REQUEST)

    # Filter recipes based on the specified search query
    recipes = Recipe.objects.filter(Q(title__icontains=search_query))
    serializer = RecipeSerializer(recipes, many=True, context={'request': request})

    if not recipes:
        return Response("No recipes found.", status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data, status=status.HTTP_200_OK)