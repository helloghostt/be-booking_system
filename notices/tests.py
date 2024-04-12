from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Notice

User = get_user_model()

class NoticeModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            is_staff=True
        )

    def test_notice_creation(self):
        notice = Notice.objects.create(
            title='Test Notice',
            content='This is a test notice.',
            author=self.user
        )
        self.assertIsInstance(notice, Notice)
        self.assertEqual(notice.title, 'Test Notice')
        self.assertEqual(notice.content, 'This is a test notice.')
        self.assertEqual(notice.author, self.user)