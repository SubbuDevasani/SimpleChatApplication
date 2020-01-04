from channels.generic.websocket import AsyncWebsocketConsumer
import json
# Inheriting the AsyncWebsocketConsumer from the channels module
""""
-----------------------------------------------------------------------------------
--> A channel is a mailbox where messages can be sent to. Each channel has a name. 
--> Anyone who has the name of a channel can send a message to the channel.
-----------------------------------------------------------------------------------
"""

class ChatConsumer(AsyncWebsocketConsumer):
    # Using the async to allow the multiple request at the same time.
    async def connect(self):
        # Every user has a scope that contains information about its connection.
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # Constructing a channels group name from the user-specified room name.
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        
        # Userd to call asynchronous functions that perform I/O. And accepts the web socket connection.
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        # the name of this method is invoked on users that receive the message.
        # Storing the user-specified message and converting to the json and sending to the group.
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send( self.room_group_name, { 'type': 'chat_message','message': message })

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({ 'message': message }))
