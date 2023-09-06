from django.urls import path, include
from rest_framework import routers
from reciperadar.views import UserViewSet, RecipeViewSet, SavedRecipeViewSet, ReviewViewSet, searchRecipes

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'savedrecipes', SavedRecipeViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Custom action for retrieving a user profile by username
urlpatterns += [
    path('users/username/<str:username>/', UserViewSet.as_view({'get': 'getByUsername'}), name='user-get-by-username'),
    path('reviews/recipe/<str:recipe>/', ReviewViewSet.as_view({'get': 'getByRecipe '}), name='review-get-by-recipe'),
    path('recipe/search/', searchRecipes, name='search'),
]
