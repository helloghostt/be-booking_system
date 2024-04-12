from django.test import TestCase
from django.contrib.auth import get_user_model
# from django.urls import reverse

User = get_user_model()

# class SignupTests(TestCase):
#     def test_signup_url_exists(self):
#         response = self.client.get(reverse('signup'))
#         self.assertEqual(response.status_code, 200)

#     def test_signup_form(self):
#         response = self.client.post(reverse('signup'), {
#             'username': 'testuser',
#             'password1': 'testpassword',
#             'password2': 'testpassword',
#         })
#         self.assertEqual(response.status_code, 302)
#         self.assertTrue(User.objects.filter(username='testuser').exists())

# class LoginTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')

#     def test_login_url_exists(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)

#     def test_login_form(self):
#         response = self.client.post(reverse('login'), {
#             'username': 'testuser',
#             'password': 'testpassword',
#         })
#         self.assertEqual(response.status_code, 302)
        
class UserModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            level=2
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.level, 2)