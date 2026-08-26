from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_ors),
    path('display/', views.display),
    path('welcome/', views.welcome),
]
