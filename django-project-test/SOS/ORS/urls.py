from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('testOrs/', views.test_ors),
    path('welcome/', views.welcome),
    path('register/', views.test_user_signup)
]
