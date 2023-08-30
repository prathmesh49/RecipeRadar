from django.shortcuts import render
from rest_framework import viewsets
from reciperadar.models import UserProfile
from reciperadar.serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset= UserProfile.objects.all()
    serializer_class= UserSerializer