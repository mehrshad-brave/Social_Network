from django.db import models


class ModelNotification(models.Model):
  message = models.TextField(max_length=300)
  
  def __str__(self):
    return self.message[0:10]