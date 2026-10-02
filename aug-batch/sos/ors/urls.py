from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('logout/', views.user_logout),
    path('<page>/', views.action), # page = Welcome
    path('<page>/<operation>/<int:id>/', views.action),
]
