from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test),
    path('register/', views.register_user),
]
