from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.user_signup, name="SIGN_UP"),
    path('login/', views.user_signin, name="SIGN_IN"),
    path('welcome/', views.welcome, name="WELCOME"),
    path('logout/', views.user_logout, name="LOG_OUT"),
    path('marksheet/', views.add_marksheet),
    path('list/', views.marksheet_list),
    path('edit/<int:id>', views.edit_marksheet),
    path('delete/<int:id>', views.delete_marksheet),
    path('logger/', views.test_logging),
]
