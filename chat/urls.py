from django.urls import path

from . import consumers


urlpatterns = [
    path('/chat/<str:room_name>', consumers.ChatConsumer)
]