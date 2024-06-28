from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test),
    path('register/', views.register_user),
    path('testList/', views.test_list),
    path('signIn/', views.user_signin),
    path('welcome/', views.welcome),
    path('save/', views.save_user),
    path('list/', views.user_list),
    path('edit/<int:id>/', views.edit_user),
    path('logout/', views.logout),
]
