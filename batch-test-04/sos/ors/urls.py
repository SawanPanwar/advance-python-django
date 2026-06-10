from django.urls import path
from . import views

urlpatterns = [
    path('testOrs/', views.test_ors),
    path('', views.welcome),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('testlist/', views.test_list),
    path('logout/', views.user_logout),
    path('list/', views.user_list),
    path('save/', views.user_save),
    path('delete/<int:id>/', views.delete_user),
    path('save/<int:id>/', views.user_save),
]
