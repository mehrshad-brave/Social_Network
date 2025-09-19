from django.urls import path, include

urlpatterns = [
  path('api/v1/', include('acconts.api.v1.urls')),
  path('', include('django.contrib.auth.urls')),
]
