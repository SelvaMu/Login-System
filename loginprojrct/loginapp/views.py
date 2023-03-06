from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.


def home(request):
    return render(request,'home.html')

def regis(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['pass']
        pass2=request.POST['repass']
        if pass1==pass2:
            if User.objects.filter(username=name).exists():
                messages.info(request,"User is Already Exists")
                return redirect('regis')
            else:
                user=User.objects.create_user(username=name,email=email,password=pass1)
                user.set_password(pass1)
                user.is_staff=True
                user.save()
                return redirect('login')
    else:
        return render(request,'registratoin.html')

def login(request):
    if request.method=='POST':
        name=request.POST['name']
        pass1=request.POST['pass']
        user=auth.authenticate(username=name,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"User name or Password is wrong")
            return redirect("login")
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')