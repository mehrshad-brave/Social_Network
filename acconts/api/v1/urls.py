from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'api-v1'

urlpatterns = [
  # registartion
  path('register/', views.RegisterApiView.as_view(), name='register'),
  path('logout/', views.Logout.as_view(), name='logout'),
  path('change/', views.ChangePasswordView.as_view(), name='change'),
  path('profile/', views.ProfileApiView.as_view(), name='profile'),
  path('user-verifi/<str:token>', views.VerifiredApiUserView.as_view(), name='verified'),
  # Email
  path('email/', views.TestEmail.as_view(), name='email'),
  # JWT 
  path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]