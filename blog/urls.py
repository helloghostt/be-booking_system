from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListCreateView.as_view(), name='post_list_create'),
    path('<int:post_id>/', views.PostRetrieveView.as_view(), name='post_retrieve'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:post_id>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:post_id>/delete/', views.PostDestroyView.as_view(), name='post_delete'),
    path('<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='comment_list_create'),
    path('<int:post_id>/comments/<int:comment_id>/', views.CommentUpdateDestroyView.as_view(), name='comment_update_destroy'),
]