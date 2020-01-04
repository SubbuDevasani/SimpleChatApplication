# Importng the path module from the django 
from django.urls import path
# Importing the views to acess the functions.
from chatroom import views
urlpatterns = [
    # keeping the first '' empty because it refers to the home
    # calling the home page in views class in chat rooom app
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # Receving the room name as a request from the project urls and refering to the room function in the views.
    path('<str:room_name>/', views.room, name='room'),

]
