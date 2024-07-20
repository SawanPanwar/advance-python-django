from django.shortcuts import render, redirect
from .ctl.WelcomeCtl import WelcomeCtl
from .ctl.LoginCtl import LoginCtl
from .ctl.UserCtl import UserCtl
from .ctl.UserListCtl import UserListCtl
from .ctl.LogoutCtl import LogoutCtl


def index(request):
    return render(request, 'index.html')


def action(request, page=""):
    if request.session.get('user') is not None and page != "":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request)
    elif page == "User":
        ctlName = "User" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request)
    elif page == "Welcome":
        ctlName = "Welcome" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request)
    else:
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request)
    return res

def actionId(request, page="", operation="", id=0):
    if request.session.get('user') is not None and page != "":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, operation, id)
    return  res
