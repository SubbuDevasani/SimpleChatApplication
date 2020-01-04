# importing the path from the django for routing flow.
from django.urls import path
# importing the views class from the accounts app for calling the below finctions.
from accounts import views
from django.conf.urls import url

# Storing the list of the paths in urlpatterns called by the project urls.py every time while running the project.
urlpatterns = [
    
    #receiving the login request, according to that calling the login function in the views.py in accounts app
    path('login',views.login,name="login"),
    
    #receiving the logout request, according to that calling the function named logout in the views.py in the account app
    path('logout',views.logout,name="logout"),
    
    #receiving the register request, according to that calling the function named register in the views.py in the account app
    path('register',views.register,name="register"),
    
    #receiving the resetpassword request, according to that calling the function named resetpassword in the views.py in the account app
    path('resetpassword',views.resetpassword,name='resetpassword'),
    
    #receiving the active request along with token , according to that calling the function named active in the views.py in the account app
    path('activate/<token>',views.activate, name='activate'),
    
    #receiving the reset request along with the token, according to that calling the function named reset in the views.py in the account app
    path('reset/<token>',views.reset, name='reset'),
    
    path('reset_password',views.reset_password,name='reset_password'),

]