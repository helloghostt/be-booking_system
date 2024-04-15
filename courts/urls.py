from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourtListCreateView.as_view(), name='court_list_create'),
    path('<int:pk>/', views.CourtRetrieveView.as_view(), name='court_retrieve'),
]