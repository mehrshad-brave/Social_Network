from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime
from posts.models import (
  Posts, 
  Comments,
  Images,
  CustomMtoMLike
  )
from acconts.models import Userx


class TestModel(TestCase):
  
  def setUp(self):
    self.create_post = Posts.objects.create(
      name = 'mehrshad',
      slug = 'mehrshad',
      time_create = datetime.now()
    )
    self.user_create_like = Userx.objects.create(username='mehrshad', password='AsasasAs@')
  
  def test_create_model_post(self):
    self.assertTrue(self.create_post.name)
    
  def test_create_model_comments(self):
    create_comment = Comments.objects.create(
      post = self.create_post,
      comment = 'mehrshad',
      time_create = datetime.now()
    )
    self.assertTrue(create_comment.comment)
    
  def test_create_model_images(self):
    create_comment = Images.objects.create(
      post = self.create_post,
      time_create = datetime.now()
    )
    self.assertTrue(create_comment.post)
    
  def test_create_model_customMtoMLike(self):
    create_comment = CustomMtoMLike.objects.create(
      like_to = self.create_post,
      to_like = self.user_create_like,
      time_create = datetime.now()
    )
    self.assertTrue(create_comment.like_to)