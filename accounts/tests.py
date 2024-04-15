from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/accounts/signup/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/accounts/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_profile(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=user)
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)