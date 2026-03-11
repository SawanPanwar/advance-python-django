from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test_ors),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
]
