from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
  class Meta:
    model = Posts 
    fields = ['name', 'slug']