from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Booking
from courts.models import Court
from accounts.models import User

class BookingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.court = Court.objects.create(name='Test Court')

    def test_create_booking(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'court': self.court.id,
            'start_time': '2023-06-01T10:00:00Z',
            'end_time': '2023-06-01T11:00:00Z'
        }
        response = self.client.post('/bookings/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_bookings(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_booking(self):
        booking = Booking.objects.create(user=self.user, court=self.court, start_time='2024-04-01T10:00:00Z', end_time='2024-04-01T11:00:00Z')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/bookings/{booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)