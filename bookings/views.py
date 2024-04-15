from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer

class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(user=user)

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingRetrieveView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

    # @action(detail=False, methods=['post'])
    # @login_required
    # def create_booking(self, request):
    #     if request.method == 'POST':
    #         form = BookingForm(request.POST)
    #         if form.is_valid():
    #             booking = form.save(commit=False)
    #             booking.user = request.user
    #             booking.save()
    #             serializer = self.get_serializer(booking)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         form = BookingForm()
    #         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class BookingCreateView(CreateView):
#     model = Booking
#     form_class = BookingForm
#     success_url = '/bookings/'  # 예약 생성 후 리디렉션할 URL