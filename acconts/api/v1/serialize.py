from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ...models import UserX, ProfileUserX

class RegisterSerialize(serializers.ModelSerializer):
  
  class Meta:
    model = UserX
    fields = ['username', 'password']
    
  
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    valid_data = super().validate(attrs)
    valid_data['text'] = "bnbccc"
    print(valid_data)
    return valid_data
  
  
class ChangePasswordSerialize(serializers.Serializer):
  old_password = serializers.CharField(required=True)
  new_password = serializers.CharField(required=True)
  new_password1 = serializers.CharField(required=True)
  
  def validate(self, data):
    if data['new_password'] != data['new_password1']:
      raise serializers.ValidationError({"error": _("new_password1 not = new_password")})
    return data
    

class ProfileSelialize(serializers.ModelSerializer):
  user = serializers.CharField(source='user.username', read_only=True)
  create_l = serializers.CharField(source='create', read_only=True)
  update_l = serializers.CharField(source='update', read_only=True)
  class Meta:
    model = ProfileUserX
    fields = ('user', "name", 'email', 'image', 'phone', 'sex', 'bio', 'create_l', 'update_l')
    #read_only_fields = ['create', 'name']