from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('logout/', views.user_logout),
]
