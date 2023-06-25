from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from media_app.models import User

def sign_up(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]

        if User.objects.filter(username=username).exists():
            print("username already exists")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            print("email already exists")
            return redirect('signup')
        
        user=User.objects.create_user(username=username, password=password)
        user=auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            print("user created successfully",user)
        else:
            print("some error is there")
    else:
        print("some error is there")

def sign_in(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            print("user is logged in", user)
        else:
            print("Some error is there")
    else:
        print("get method for sign in")
        print("render sign in html page")

def sign_out(request):
    auth.logout(request)
    print("logout is done")