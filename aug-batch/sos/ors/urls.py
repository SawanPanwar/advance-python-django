from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_ors),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('logout/', views.user_logout),
    path('testlist/', views.test_list),
    path('list/', views.user_list),
    path('delete/<int:id>/', views.delete_user),
    path('save/', views.user_save),
    path('edit/<int:id>/', views.edit_user),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('destroy/', views.destroy_session),
    path('set/', views.set_cookies),
    path('get/', views.get_cookies),
]
