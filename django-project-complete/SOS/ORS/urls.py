from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<page>/', views.action),
    path('auth/<page>/', views.auth),
]
