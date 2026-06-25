from django.shortcuts import render, redirect
from .ctl.registration_ctl import RegistrationCtl
from .ctl.login_ctl import LoginCtl
from .ctl.welcome_ctl import WelcomeCtl
from .ctl.user_ctl import UserCtl
from .ctl.user_list_ctl import UserListCtl
from .ctl.role_ctl import RoleCtl
from .ctl.role_list_ctl import RoleListCtl


def welcome(request):
    return render(request, 'welcome.html')


def user_logout(request):
    request.session.flush()
    return redirect('/ors/Login/')


def action(request, page):
    ctl_name = page + "Ctl()"
    ctl_obj = eval(ctl_name)
    return ctl_obj.execute(request, params={'operation': '', 'id': 0})


def action_operation_id(request, page, operation='', id=0):
    ctl_name = page + "Ctl()"
    ctl_obj = eval(ctl_name)
    return ctl_obj.execute(request, params={'operation': operation, 'id': id})
