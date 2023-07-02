from django.urls import path
from media_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('signout/', views.sign_out, name='sign_out'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('add_post/', views.add_post, name='add_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
]