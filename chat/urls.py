from django.urls import path

from . import consumers

app_name = "chat" 

urlpatterns = [
    path('/chat/<room_name>', consumers.ChatConsumer)
]