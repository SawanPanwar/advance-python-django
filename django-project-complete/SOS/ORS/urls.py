from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<page>/', views.action),
    path('<page>/<operation>/<int:id>', views.action),
]
