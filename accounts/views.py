from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user_name = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        if password == confirm_password:
            if User.objects.filter(username = user_name).exists():
                messages.info(request,'Username Already Exist')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,password=password,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password Not match')
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['uname']
        password = request.POST['pass1']
        
        user = auth.authenticate(username = user_name,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
                
        else:
            messages.info(request,'Invalid  Credentials')
            return redirect('login')
    
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')
    