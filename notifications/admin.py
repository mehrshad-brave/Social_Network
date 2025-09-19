from django.contrib import admin
from django import forms
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponseRedirect
from django.urls import path
from .models import ModelNotification


class NotificationForm(forms.Form):
  messagef = forms.CharField(label='message', max_length=300)
  
  
@admin.register(ModelNotification)
class NotificationAdmin(admin.ModelAdmin):
  add_form_template = "admin/admin_add_template.html"
  change_form_template = "admin/admin_add_template.html"
  
  def add_view(self, request, form_url="", extra_context=None):
    if request.method == "POST":
      form = NotificationForm(request.POST)
      if form.is_valid():
        message = form.cleaned_data['messagef']
        
        notification = ModelNotification.objects.create(message=message)
        
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
          'notification',
          {
            'type': "send_notification",
            'message': message
          }
        )
        
        return HttpResponseRedirect("../{}/".format(notification.pk))
        
    else:
      form = NotificationForm()
      
    context = self.get_changeform_initial_data(request)
    context['form'] = form
    return super().add_view(request, form_url, extra_context=context)
    
  def get_urls(self):
    urls = super().get_urls()
    custom_url = [
      path('send-notification/', self.admin_site.admin_view(self.add_view), name="send-notification"),
    ]
    return custom_url + urls