from rest_framework import serializers
from ...models import Posts

class PostsSerializers(serializers.ModelSerializer):
  # comments = serializers.CharField(source='comment_post')
  mark = serializers.CharField(source='marke.username', read_only=True)
  apsoluat_url = serializers.SerializerMethodField()
  class Meta:
    model = Posts
    fields = ['id', 'apsoluat_url', 'mark', 'name', 'time_create', 'time_update']
  
  def get_apsoluat_url(self, obj):
    #print(f"\n{obj}\n")
    ur = self.context.get("request")
    print(ur, '\n')
    return ur
    
  def to_representation(self, data):
    obj = super().to_representation(data)
    print(obj)
    return obj
    
  def create(self, validated_data):
    obj = self.context.get('request')
    print(obj)
    return super().create(validated_data)