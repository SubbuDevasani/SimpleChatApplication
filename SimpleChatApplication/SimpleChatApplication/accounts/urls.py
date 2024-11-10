# Importing the path from Django for routing flow
from django.urls import path
# Importing the views class from the accounts app for calling the below functions
from accounts import views

# Storing the list of the paths in urlpatterns called by the project urls.py every time while running the project
urlpatterns = [
    # Receiving the login request, according to that calling the login function in the views.py in accounts app
    path('login/', views.login, name="login"),
    
    # Receiving the logout request, according to that calling the function named logout in the views.py in the account app
    path('logout/', views.logout, name="logout"),
    
    # Receiving the register request, according to that calling the function named register in the views.py in the account app
    path('register/', views.register, name="register"),
    
    # Receiving the resetpassword request, according to that calling the function named resetpassword in the views.py in the account app
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    
    # Receiving the activate request along with token, according to that calling the function named activate in the views.py in the account app
    path('activate/<token>/', views.activate, name='activate'),
    
    # Receiving the reset request along with the token, according to that calling the function named reset in the views.py in the account app
    path('reset/<token>/', views.reset, name='reset'),
    
    # Receiving the reset_password request, according to that calling the function named reset_password in the views.py in the account app
    path('reset_password/', views.reset_password, name='reset_password'),
]

