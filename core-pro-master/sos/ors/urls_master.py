from django.contrib import admin
from django.urls import path
from . import views_master

urlpatterns = [
    path('', views_master.welcome),
    path('welcome/', views_master.welcome),
    path('signup/', views_master.user_signup),
    path('signin/', views_master.user_signin),
    path('logout/', views_master.user_logout),
    path('list/', views_master.user_list),
    path('delete/<int:id>/', views_master.delete_user),
    path('save/', views_master.user_save),
    path('save/<int:id>/', views_master.user_save),
]

