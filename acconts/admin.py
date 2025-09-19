from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from acconts.models import UserX, ProfileUserX
from acconts.forms import UserCreationForm, UserChangeForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  add_form = UserCreationForm
  
  list_display = ['username']
  list_filter = ['username']
  
  fieldsets = [
   ('UserX', {'fields':['username', 'password']
   }
   ),
   ('Permission', {
     'fields': ['is_superuser', 'is_staff', 'is_activ', 'is_verified']
     }
    ),
  ]
  add_fieldsets = [
    ('UserX', {
      'classes': ['wide'], 
      'fields': ['username', 'password1', 'password2']
      }
    ),
  ]
  search_field = ['username']
  ordering = ['username']
  filter_horizontal = []
  

admin.site.register(UserX, UserAdmin)
#admin.site.unregister(ProfileUserX)
@admin.register(ProfileUserX)
class AdminP(admin.ModelAdmin):
  pass
admin.site.unregister(Group)