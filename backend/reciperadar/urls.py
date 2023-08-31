
from django.urls import path, include
from .views import UserViewSet, RecipeViewSet, SavedRecipeViewSet, ReviewViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'savedrecipes', SavedRecipeViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]
