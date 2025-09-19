from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.utils.translation import gettext_lazy
from django.contrib.admin.decorators import action
from django.template.response import TemplateResponse
from .models import (Posts, Comments, Images, CustomMtoMLike)


class ChildPostComment(InlineModelAdmin):
  model = Comments
  extra = 1
  #template = "admin_inlines/comments.html"
  template = "admin/edit_inline/tabular.html"
  

class ChildPostImage(InlineModelAdmin):
  model = Images
  extra = 1
  template = "admin/edit_inline/tabular.html"

class ChildPostLike(InlineModelAdmin):
  model = CustomMtoMLike
  extra = 2
  template = "admin/edit_inline/tabular.html"
  
@action(description=gettext_lazy("activate posts"))
def test_action(modeladmin, request, queryset):
   queryset.update(bad_admin=True)
   
  
@action(description=gettext_lazy("deactivate posts"))
def deactiv_posts(modeladmin, request, queryset):
  queryset.update(bad_admin=False)
  

class PostAdmin(admin.ModelAdmin):
  add_form_template = "admin_custom/post_change_form_object.html" 
  change_form_template = "admin_custom/posts_change_form.html"
  raw_id_fields = ['marke']
  list_display = ['marke']
  list_filter = ['marke']
  ordering = ['time_create']
  #change_list_template =  "admin_inlines/comments.html"
  inlines = (ChildPostComment, ChildPostLike, ChildPostImage)
  actions = [test_action, deactiv_posts]
  
  
  
admin.site.register(Posts, PostAdmin)

@admin.register(Comments)
class B(admin.ModelAdmin):
  pass

@admin.register(Images)
class I(admin.ModelAdmin):
  pass

@admin.register(CustomMtoMLike)
class Y(admin.ModelAdmin):
  pass