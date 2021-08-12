import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        '''
        Connects the client
        '''

        # Gets chatroom name
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Joins the chatroom
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # informs the client 
        await self.accept()

    async def disconnect(self, close_code):
        '''
        Disconnets the client
        '''

        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        '''
        The client sends the info and we get the info
        '''

        text_data_json = json.load(text_data)
        name = text_data_json["name"]
        text = text_data_json["text"]

        # Send the message to the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "name": name,
                "text": text,
            },
        )
    
    async def chat_message(self, event):
        '''
        We get room info
        '''

        name = event["name"]
        text = event["text"]

        await self.send(
            text_data=json.dumps(
                {
                    "type": "chat_message",
                    "name": name,
                    "text": text,
                }
            )
        )