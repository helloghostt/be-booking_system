# public class ReservationInfo {
#     private LocalDateTime start; // 예약 시작 시간
#     private LocalDateTime end; // 예약 종료 시간
#     private ReservationStatus status; // 예약 상태 RESERVED, FINISHED
#     private Boolean regular; // 정기 예약 여부
# }


from django.urls import path, include
from rest_framework import routers
from .views import BookingViewSet, BookingCreateView

router = routers.DefaultRouter()
router.register('bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='booking_create'),
    # 다른 URL 패턴들이 있다면 여기에 추가
] + router.urls