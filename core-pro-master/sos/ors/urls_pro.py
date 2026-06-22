from django.contrib import admin
from django.urls import path
from . import views_pro

urlpatterns = [
    path('', views_pro.welcome),
    path('welcome/', views_pro.welcome),
    path('signup/', views_pro.user_signup),
    path('signin/', views_pro.user_signin),
    path('logout/', views_pro.user_logout),
    path('list/', views_pro.user_list),
    path('delete/<int:id>/', views_pro.delete_user),
    path('save/', views_pro.user_save),
    path('save/<int:id>/', views_pro.user_save),
]

