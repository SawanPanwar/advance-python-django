from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('testOrs/', views.test_ors),
    path('welcome/', views.welcome),
    path('register/', views.test_user_signup),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('logout/', views.logout),
    path('testList/', views.test_list),
    path('list/', views.user_list),
    path('delete/<int:id>/', views.delete_user),
    path('save/', views.user_save),
    path('edit/<int:id>/', views.edit_user),
]