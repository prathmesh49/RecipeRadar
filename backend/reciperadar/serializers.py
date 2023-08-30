from rest_framework import serializers

from reciperadar.models import UserProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'