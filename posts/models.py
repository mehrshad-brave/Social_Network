from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jalali

User = get_user_model()
# Create your models here.

class Posts(models.Model):
  name = models.CharField(max_length=300)
  marke = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="marke_post")
  slug = models.SlugField()
  bad_admin = models.BooleanField(default=True)
  like = models.ManyToManyField(through='CustomMtoMLike', to=User, related_name="like_post_user")
  
  # Data
  time_create = jalali.jDateTimeField(auto_now_add=True)
  time_update = jalali.jDateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name if self.name else self.marke.email
  
class CustomMtoMLike(models.Model):
  like_to = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="like_to")
  to_like = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_like")
  
  # Data
  time_create = jalali.jDateTimeField(auto_now_add=True)
  
  def __str__(self):
    return 'user {} liked a post called {}'.format(self.to_like, self.like_to)
  
  
class Comments(models.Model):
  post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comment_post')
  comment = models.TextField(max_length=2000)
  
  # Data
  time_create = jalali.jDateTimeField(auto_now_add=True)
  time_update = jalali.jDateTimeField(auto_now=True)
  
  def __str__(self):
    return self.comment[0:20]
    
    
class Images(models.Model):
  post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='image_post')
  image = models.ImageField(blank=True, null=True, upload_to="images")
  
  # Data
  time_create = jalali.jDateTimeField(auto_now_add=True)
  time_update = jalali.jDateTimeField(auto_now=True)
  
  