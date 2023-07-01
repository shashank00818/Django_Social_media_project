from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from media_app.models import User, Post, LikePost
from django.contrib.auth.decorators import login_required
from media_app.utils import find_no_of_likes_received_by_user

def index(request):
    user = request.user
    page_name="index.html"
    data = {
        "post_list" : Post.objects.all().order_by('-created_at'),
        "already_liked_post_ids_of_current_user": user.like_post.values_list('post_id', flat=True)
    }
    return render(request, page_name, data)

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
            return redirect('index')
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
            return redirect('index')
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
    user = request.user
    page_name="profile_settings.html"
    data = {
        "no_of_posts_created" : user.post.count(),
        "no_of_likes_done": user.like_post.count(),
        "no_of_likes_received": find_no_of_likes_received_by_user(user),
    }
    return render(request, page_name, data)

@login_required(login_url='sign_in')
def add_post(request):
    user = request.user
    caption = request.POST['caption']
    Post.objects.create(user=user, caption=caption)
    return redirect('index')

@login_required(login_url='sign_in')
def like_post(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    LikePost.objects.create(
        post_id=post_id,
        user_id=user.id
    )
    return redirect('index')