from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ...models import Posts

from .serializer import PostsSerializers

class PostsApiView(generics.GenericAPIView):
  serializer_class = PostsSerializers
  queryset = Posts.objects.all()
  def get(self, request, *args, **kwargs):
    user = self.get_queryset()
    sr = self.get_serializer_class()
    serializer = sr(user, many=True)
    return Response(serializer.data, status=200)
    
  def post(self, request, *args, **kwargs):
    user = self.get_queryset()
    sr = self.get_serializer_class()
    serializer = sr(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=200)
    

class PostsDetailApiView(generics.GenericAPIView):
  serializer_class = PostsSerializers
  
  def get(self, request, pk,  *args, **kwargs):
    user = get_object_or_404(Posts, pk=pk)
    sr = self.get_serializer_class()
    serializer = sr(user)
    return Response(serializer.data, status=200)
    
  def put(self, request, pk,  *args, **kwargs):
    user = get_object_or_404(Posts, pk=pk)
    sr = self.get_serializer_class()
    serializer = sr(user, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=200)
    
  def delete(self, request, pk,  *args, **kwargs):
    user = get_object_or_404(Posts, pk=pk)
    user.delete()
    return Response({'detail': 'delit post ok'}, status=200)