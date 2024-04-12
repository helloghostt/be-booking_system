from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Booking
from courts.models import Court

User = get_user_model()

class BookingModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.court = Court.objects.create(name='Test Court')

    def test_booking_creation(self):
        start_time = timezone.now()
        end_time = start_time + timezone.timedelta(hours=1)
        booking = Booking.objects.create(
            user=self.user,
            court=self.court,
            start_time=start_time,
            end_time=end_time
        )
        self.assertIsInstance(booking, Booking)
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.court, self.court)
        self.assertEqual(booking.start_time, start_time)
        self.assertEqual(booking.end_time, end_time)