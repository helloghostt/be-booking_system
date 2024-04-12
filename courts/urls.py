# be/courts/urls.py

from django.urls import path
from . import views

app_name = 'courts'

urlpatterns = [
    path('list/', views.court_list, name='court_list'),
    # 다른 URL 패턴이 필요하다면 여기에 추가
]