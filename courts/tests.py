from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Court

class CourtTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_court(self):
        data = {
            'name': 'Test Court',
            'description': 'This is a test court'
        }
        response = self.client.post('/courts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_courts(self):
        Court.objects.create(name='Court 1', description='Description 1')
        Court.objects.create(name='Court 2', description='Description 2')
        response = self.client.get('/courts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_court(self):
        court = Court.objects.create(name='Test Court', description='Test Description')
        response = self.client.get(f'/courts/{court.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Court')