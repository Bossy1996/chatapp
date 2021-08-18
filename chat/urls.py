from django.urls import path

from . import consumers


urlpatterns = [
    path('/chat/<room_name>', consumers.ChatConsumer)
]