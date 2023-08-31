from rest_framework import serializers

from reciperadar.models import UserProfile, Recipe, SavedRecipe, Review

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_id=serializers.ReadOnlyField()
    class Meta:
        model=UserProfile
        fields='__all__'
        
class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_id=serializers.ReadOnlyField()
    class Meta:
        model=Recipe
        fields='__all__'
        
class SavedRecipeserializer(serializers.HyperlinkedModelSerializer):
    saved_recipe_id= serializers.ReadOnlyField()
    class Meta:
        model= SavedRecipe
        fields='__all__'
        
class ReviewSearializers(serializers.HyperlinkedModelSerializer):
    review_id= serializers.ReadOnlyField()
    class Meta:
        model= Review
        fields='__all__'