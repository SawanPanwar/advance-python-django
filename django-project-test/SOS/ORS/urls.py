from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test_ors),
    path('testSignUp/', views.test_user_signup),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
]
