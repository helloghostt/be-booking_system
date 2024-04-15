from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post, Comment
from accounts.models import User

class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_create_post(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Post',
            'content': 'New Content',
            'image': open('path/to/test/image.jpg', 'rb')
        }
        response = self.client.post('/blog/create/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_post(self):
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Updated Post',
            'content': 'Updated Content'
        }
        response = self.client.put(f'/blog/{self.post.id}/edit/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/blog/{self.post.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_create_comment(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'content': 'Test Comment'
        }
        response = self.client.post(f'/blog/{self.post.id}/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_comments(self):
        response = self.client.get(f'/blog/{self.post.id}/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        comment = Comment.objects.create(post=self.post, content='Test Comment', author=self.user)
        self.client.force_authenticate(user=self.user)
        data = {
            'content': 'Updated Comment'
        }
        response = self.client.put(f'/blog/{self.post.id}/comments/{comment.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        comment = Comment.objects.create(post=self.post, content='Test Comment', author=self.user)
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/blog/{self.post.id}/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)