from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('logout/', views.user_logout),
    path('html/', views.test_html_utility),
    path('<page>/', views.action),
    path('<page>/<operation>/<int:id>/', views.action_operation_id),
]
