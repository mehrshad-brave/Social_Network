from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.template import Template, Context

class NotificationConsum(AsyncJsonWebsocketConsumer):
  async def connect(self):
    await self.connect()
    await self.channel_layer.group_add('notification', self.channel_name)
    
  async def disconnect(self, close_code):
    await self.channel_layer.group_discard('notification', self.channel_name)
    
  async def send_notification(self, event):
    messages = event['messages']
    
    template = Template('<div class="notification_class"><p>{{messages}}</p></div>')
    context = Context({'messages': messages})
    render_notifucation = template.render(context)
    
    await self.send(
      text_data=json.dumps(
        {
          'type': 'notification',
          'message': render_notifucation
        }
        )
    )