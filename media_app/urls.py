from django.urls import path
from media_app import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('signout/', views.sign_out, name='sign_out'),
    path('profile-settings/', views.profile_settings, name='profile_settings'),
]