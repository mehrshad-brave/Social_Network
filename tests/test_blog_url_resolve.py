from django.test import TestCase
from django.urls import reverse, resolve
from posts.views import Index
from posts.forms import PostsForm

# Create your tests here.
class TestUrl(TestCase):
  def test_blog_url(self):
    url = reverse('custom_url_admin:index_test')
    self.assertEqual(resolve(url).func.view_class, Index, msg=None)
    
    
class TestForm(TestCase):
   def test_form_posts_create_true(self):
     form = PostsForm(data={
       'name': 'mehrshad',
       'slug': 'mehrshad',
     })
     self.assertTrue(form.is_valid())
     
   def test_form_posts_create_false(self):
      form = PostsForm(data={})
      self.assertFalse(form.is_valid())