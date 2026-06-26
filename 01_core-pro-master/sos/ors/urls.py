from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('<page>/', views.action), # page = Registration
]
