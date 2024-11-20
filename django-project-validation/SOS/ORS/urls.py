from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('signUp/', views.user_signup),
    path('login/', views.user_signin),
    path('save/', views.user_save),
    path('testList/', views.test_list),
    path('list/', views.user_list),
    path('edit/<int:id>/', views.edit_user),
    path('delete/<int:id>/', views.delete_user),
    path('logout/', views.logout),
]
