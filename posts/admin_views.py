from django.shortcuts import render, get_object_or_404
from .models import (Posts, Images, Comments, CustomMtoMLike)

# Create your views here.

def runposts(request):
  return render(request, "posts/posts.html")
  
  
def post_guide(request, id, ret):
  user = get_object_or_404(Posts, id=id)
  if request.method == "GET":
    if ret == "Comments":
      return render(request, "admin_inlines/images.html", {"comments":Comments.objects.filter(post=user), "id_post":user.id})
      
      
def add_comment(request, post_id):
  user = get_object_or_404(Posts, id=post_id)
  