from django.urls import path, include
from . import admin_views
from . import views

app_name = "custom_url_admin"

urlpatterns = [
  # _____________Api_______________ #
  
  path('api/v1/', include('posts.api.v1.urls')),
  path("test/post/change/<int:id>/<str:ret>/", admin_views.post_guide, name="post_guide"),
  path("add/comment/<int:post_id>/change", admin_views.add_comment, name="add_comment"),
  
  # _____________Posts_______________ #
  
  path('list/post/', views.ListPostDistroyCreate.as_view(), name="list_posts"),
]