from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test),
    path('register/', views.register_user),
    path('testList/', views.test_list),
    path('signIn/', views.user_signin),
    path('welcome/', views.welcome),
]
