# Importing the path module from Django
from django.urls import path
# Importing the views to access the functions
from chatroom import views

urlpatterns = [
    # Keeping the first '' empty because it refers to the home
    # Calling the home page in views class in chatroom app
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    # Receiving the room name as a request from the project URLs and referring to the room function in the views
    path('<str:room_name>/', views.room, name='room'),
]

