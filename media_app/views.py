from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from media_app.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    page_name="index.html"
    return render(request, page_name)

def sign_up(request):
    page_name='sign_up.html'
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, page_name, {"error":True,"error_msg":"User already exists"})
        
        if User.objects.filter(email=email).exists():
            return render(request, page_name, {"error":True,"error_msg":"Email already exists"})
        
        user=User.objects.create_user(username=username, password=password)
        user=auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('profile_settings')
        else:
            return render(request, page_name, {"error":True,"error_msg":"Some error is there"})
    else:
        return render(request, page_name)

def sign_in(request):
    if request.method=="POST":
        page_name='sign_in.html'
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('profile_settings')
        else:
            return render(request, page_name, {"error":True,"error_msg":"Some error"})
    else:
        return render(request, page_name)

@login_required(login_url='sign_in')
def sign_out(request):
    auth.logout(request)
    return redirect('sign_up')

@login_required(login_url='sign_in')
def profile_settings(request):
    page_name="profile_settings.html"
    data={
        "id":request.user.id,
        "email":request.user.email,
        "username":request.user.username
    }
    return render(request, page_name, data)