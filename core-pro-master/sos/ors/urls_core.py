from django.contrib import admin
from django.urls import path
from . import views_core

urlpatterns = [
    path('', views_core.welcome),
    path('welcome/', views_core.welcome),
    path('signup/', views_core.user_signup),
    path('signin/', views_core.user_signin),
    path('logout/', views_core.user_logout),
    path('list/', views_core.user_list),
    path('delete/<int:id>/', views_core.delete_user),
    path('save/', views_core.user_save),
    path('save/<int:id>/', views_core.user_save),
]