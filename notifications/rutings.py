from django.urls import path
from posts import views
from .consumer import NotificationConsum


websocket_urlpatterns = [
  path('web/', NotificationConsum.as_asgi(), name='web_so'),
]