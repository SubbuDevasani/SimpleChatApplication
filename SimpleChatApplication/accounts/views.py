# importing the reqired modules 
from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from chatroom.tokens import Token
from django.core.mail import send_mail
from chatapp.settings import EMAIL_HOST_USER
#import redis

""""
------------------------------------------------------------------------
Request types using ::  
    --> POST==> Submits data to be processed.
    --> GET==> Requests a representation of the specified resource.
------------------------------------------------------------------------
"""


#After calling the request in  views.register in acccounts.urls the request comes here...
def register(request):
    
    #if the received request is 'POST, then the below condition satisfies
    if request.method == 'POST':
        # Storing the data receving from the register.html page in variables        
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailid = request.POST['emailid']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        # If the entered passwords are equals then the below condition satisfies.         
        if password1==password2:
            # Checking the entered username already exits in the database by using User module 
            # If the given username exits in the data base then printing the message on the page.
            if User.objects.filter(username=username).exists():
                # Printing the meassage using the messages imported from django.                 
                messages.info(request, 'Username already exits')
                # redirecting again to the register function.                 
                return redirect('register')
            
            # else, Checking the entered email id already exits in the database by using User module
            # If the given email exits in the data base then printing the message on the page.
            elif User.objects.filter(email=emailid).exists():
                messages.info(request,'email or phone number already exits')
                # redirecting again to the register function
                return redirect('register')
            
            # If the above conditions are fails..
            else:
                # Creating the user in the database by passing the details below. 
                user = User.objects.create_user(username=username, password=password1, email=emailid, first_name=firstname, last_name=lastname)
                # Making the user activation false because for verfying the user.
                user.is_active = False
                # Saving the details in the databse
                user.save()
                # taking the payload varible in the dictionary format, because for generating token
                payload={'id': username}
                # And taking the variables key and algorithm for generating the token
                key="manikanta123"
                # Mentioning the algorithm the way for creating the token
                algorithm='HS256'
                # Storing the current site means the localhost address
                current_site = get_current_site(request)
                # Taking the subject for the mail
                mail_subject = 'Activate your blog account.'
                # storing the message in the string format along with http link in the acc_active_email.html
                message = render_to_string('chatroom/acc_active_email.html', {
                'user': username,
                'domain': current_site.domain,
                 # Generating the token by sending payload, key, alogorithm
                'token':Token.encode(payload,key,algorithm),
                })
                # storing the to email address
                to_email = User.objects.get(email=emailid)
                # Sending the mail using send_mail default django function
                # Tkes the arguments subject,sending mail,to mail,message
                send_mail(mail_subject, message, EMAIL_HOST_USER ,[to_email.email])
                # After sending the mail refer to the html page
                return render(request,"registration/password_reset_done.html")
        else:
            messages.info(request,"passwords doesn't match")
            return render(request,"chatroom/register.html")
    # if the receving request is GET the it returns to the register.html page.
    else:
        return render(request,"chatroom/register.html")

    
# when the user enters the link form the mail then this activate method invokes
#After calling the request in views.active having the token in accounts.urls the request comes here...
def activate(request, token):
    # taking the variables key and algorithm for decoding the tokens     
    key="manikanta123"
    algorithm='HS256'
    
    # Decoding the token sending the key, token ,algorithm
    try:
        print("------->")
        x=Token.decode(token,key,algorithm)
        user = User.objects.get(username=x['id'])
        
    # if any error comes when decoding the token haldling the errors and taking user as none
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # If user is not none then making the user active and directing to the login.html page
    if user is not None :
        user.is_active = True
        user.save()
        messages.info(request,'Thank you for your email confirmation. Now you can login your account.')
        # calling the login function
        return redirect('login')
    else:
        # if the link is not valid then user will be none then writting the below context
        return HttpResponse('Activation link is invalid!')
    

# When the user requests for login then the request comes here for login operation..
def login(request):
    #if the received request is 'POST, then the below condition satisfies
    if request.method == 'POST':
        # Storing the data receving from the login.html page in variables
        username = request.POST['username']
        password = request.POST['password1']
        # Authenticating the user by passing the password and the password in database
        user = auth.authenticate(username=username,password=password)
        # id user is not none then redirecting to the index.html page
        if user is not None:
            # Receving the request if user is not none and passing the user for authentication
            auth.login(request, user)
            return render(request,"chatroom/index.html")
        else:
            # If the user entered the wrong username then the request arises and print in the below context in the page 
            messages.info(request, 'invalid creditionals')
            return redirect('login')
    else:
        # If the request is GET then redirecting to the login page
        return render(request,"chatroom/login.html")

    
# When the user requests for logout then the request comes here for logout operation..
def logout(request):
    # Using the default function in django sending the request for logout
    auth.logout(request)
    # After logout then redirecting to the home page
    return redirect('/')


#  When the user requests for resetpassword then the request comes here for resetpassword operation..
def resetpassword(request):
    #if the received request is 'POST, then the below condition satisfies
    if request.method == 'POST':
                # Storing the data receving from the html page in variables
                username = request.POST['username']
                email = request.POST['email']
                if User.objects.filter(username=username).exists():
                    user = User.objects.get(username=username)
                    user.is_active = False
                    user.save()
                    payload={'id': username}
                    key="manikanta123"
                    algorithm='HS256'
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your blog account.'
                    # Getting the username from the database
                    user = User.objects.get(username=username)
                    # Making the user activation false because for verfying the user.
                    user.is_active = False
                    # Saving the user data
                    user.save()
                    # taking the payload varible in the dictionary format, because for generating token
                    payload={'id': username}
                    # And taking the variables key and algorithm for generating the token
                    key="manikanta123"
                    algorithm='HS256'
                    # Storing the current site means the localhost address
                    current_site = get_current_site(request)
                    # Taking the subject for the mail
                    mail_subject = 'Activate your blog account.'
                    # storing the message in the string format along with http link in the passworda_reset_email.html
                    message = render_to_string('registration/password_reset_email.html', {
                    'user': username,
                    'domain': current_site.domain,
                    'token':Token.encode(payload,key,algorithm),
                    })
                    to_email = email
                    send_mail(mail_subject, message, EMAIL_HOST_USER ,[to_email],fail_silently = False)
                    return render(request,"registration/password_reset_done.html")
                else:
                    messages.info(request,'User does not exits')
                    return render(request,'registration/password_reset.html')
                    # Sending the mail using send_mail default django function
                    # Tkes the arguments subject,sending mail,to mail,message
                    send_mail(mail_subject, message, EMAIL_HOST_USER ,[to_email],fail_silently = False)
                    # returning to the password done page
                    return render(request,"registration/password_reset_done.html")
    else:
        # If the given request is Get the redirect to the password_reset.html page
        return render(request,'registration/password_reset.html')
    

# when the user enters the link form the mail then this reset_passowrd method invokes
#After calling the request in views.active having the token in accounts.urls the request comes here...
def reset(request,token):
    return render(request,"registration/password_reset_confirm.html")
    key="manikanta123"
    algorithm='HS256'
    try:
        x=Token.decode(token,key,algorithm)
        user = User.objects.get(username=x['id'])
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and Token.decode(token,key,algorithm):
        user.is_active = True
        user.save()
        messages.info(request,'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')
def reset_password(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        user = User.objects.get(username=username)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                user.set_password('password1')
                user.save()
                messages.info(request,'Sucessfully changed password')
                return render(request,"chatroom/login.html")
        else:
            messages.info(request,'Password not matched')
            return render(request,"registration/password_reset_confirm.html")

    else:
        return render(request,"registration/password_reset_confirm.html") 

