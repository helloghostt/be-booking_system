from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Notice
from accounts.models import User

class NoticeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword', is_staff=True)
        self.notice = Notice.objects.create(title='Test Notice', content='Test Content', author=self.user)

    def test_create_notice(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Notice',
            'content': 'New Content'
        }
        response = self.client.post('/notices/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_notices(self):
        response = self.client.get('/notices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_notice(self):
        response = self.client.get(f'/notices/{self.notice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_notice(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Updated Notice',
            'content': 'Updated Content'
        }
        response = self.client.put(f'/notices/{self.notice.id}/edit/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_notice(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/notices/{self.notice.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)