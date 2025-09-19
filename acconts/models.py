from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ManageUserX(BaseUserManager):
  def create(self, username, password, **extra):
    if not username:
      raise ValueError('You have not entered the username')
    user = self.model(username=username, **extra)
    user.set_password(password)
    user.save()
    return user
    
  def create_superuser(self, username, password, **extra):
    extra.setdefault('is_staff', True)
    extra.setdefault('is_superuser', True)
    extra.setdefault('is_activ', True)
    extra.setdefault('is_verified', True)
    
    if extra.get('is_superuser') is not True:
      raise ValueError('Super User option is not enabled')
    if extra.get('is_verified') is not True:
      raise ValueError('Super User option is not enabled')
    if extra.get('is_staff') is not True:
      raise ValueError('Employee option is not enabled')
    return self.create(username, password, **extra)
      


class UserX(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=255, unique=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_activ = models.BooleanField(default=True)
  is_verified = models.BooleanField(default=False)
  
  objects = ManageUserX()
  USERNAME_FIELD = 'username'
  
  def __str__(self):
    return self.username
  
  
class ProfileUserX(models.Model):
  class SexUser(models.TextChoices):
    MAN = 'MN', _('Man')
    WOMAN = 'WN', _('Woman')
    CUSTOM = 'CM', _('custom')
    NO = 'NO', _('I prefer not to say')
    
  user = models.OneToOneField(UserX, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, blank=True, null=True)
  phone = models.BigIntegerField(blank=True, null=True)
  email = models.EmailField(max_length=250, blank=True, null=True)
  image = models.ImageField(blank=True, null=True, upload_to = 'images/image_users')
  sex = models.CharField(max_length=2, choices=SexUser, default=SexUser.MAN)
  bio = models.TextField(max_length=1000, blank=True, null=True)
  
  # Data
  create = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name