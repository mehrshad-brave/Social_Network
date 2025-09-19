from django.views.generic.base import View, TemplateView
from django.shortcuts import get_object_or_404, render
from .models import (
  Posts,
  Comments,
  Images,
  CustomMtoMLike
)

class ListPostDistroyCreate(TemplateView):
  # template_name = 'parend/list.html'
  
  def get(self, request, *args, **kwargs):
    posts = Posts.objects.all()
    return render(request, "parend/list_posts.html", {'list':posts})