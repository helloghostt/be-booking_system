from django.test import TestCase
from .models import Court

class CourtModelTests(TestCase):
    def test_court_string_representation(self):
        court = Court.objects.create(name='Test Court')
        self.assertEqual(str(court), 'Test Court')