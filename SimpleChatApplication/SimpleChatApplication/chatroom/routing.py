from django.urls import re_path
# Importing the ChatConsumer class from the consumer module ni chatroom app
from .consumers import ChatConsumer

# Creating the websocket to managing the communicaton between the clent and the server.
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
]
