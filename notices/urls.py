from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoticeListView.as_view(), name='notice_list'),
    path('<int:pk>/', views.NoticeRetrieveView.as_view(), name='notice_retrieve'),
    path('create/', views.NoticeCreateView.as_view(), name='notice_create'),
    path('<int:pk>/edit/', views.NoticeUpdateView.as_view(), name='notice_update'),
    path('<int:pk>/delete/', views.NoticeDestroyView.as_view(), name='notice_delete'),
]