from django.urls import path

from . import views

urlpatterns = [
    path('hi/', views.test_ors),
    path('', views.welcome),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
]
