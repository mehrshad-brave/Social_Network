from django.urls import path
from . import views



urlpatterns = [
  path('posts/', views.PostsApiView.as_view(), name='posts'),
  path('posts/<str:pk>/', views.PostsDetailApiView.as_view(), name='posts'),
]