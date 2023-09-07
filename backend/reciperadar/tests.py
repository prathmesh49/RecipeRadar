from django.test import TestCase
from .models import UserProfile

class UserProfileModelTest(TestCase):
    def test_user_profile_model(self):
        # Create one or more user profiles
        user1 = UserProfile.objects.create(username='user1', password='password1', bio='Bio 1', location='Location 1', avatar_url='Avatar 1', name='Name 1')
        user2 = UserProfile.objects.create(username='user2', password='password2', bio='Bio 2', location='Location 2', avatar_url='Avatar 2', name='Name 2')

        # Check the count of user profiles in the database
        users_count = UserProfile.objects.count()
        
        # Assert that the count matches the number of user profiles created
        self.assertEqual(users_count, 2)
