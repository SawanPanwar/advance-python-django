from django.shortcuts import render
from .ctl.registration_ctl import RegistrationCtl
from .ctl.login_ctl import LoginCtl
from .ctl.welcome_ctl import WelcomeCtl


def welcome(request):
    return render(request, 'welcome.html')


def action(request, page):  # page = Registration
    ctl_name = page + "Ctl()"  # ctl_name = "RegistrationCtl()"
    ctl_obj = eval(ctl_name)  # ctl_obj = RegistrationCtl()

    if request.method == "GET":
        return ctl_obj.display(request)

    if request.method == "POST":
        return ctl_obj.submit(request)
