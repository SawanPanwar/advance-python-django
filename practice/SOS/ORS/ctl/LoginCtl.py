from django.shortcuts import render, redirect
from ..service.UserService import UserService
from .BaseCtl import BaseCtl


class LoginCtl(BaseCtl):
    def __init__(self):
        self.form = {}

    def request_to_form(self, requestForm):
        self.form["loginId"] = requestForm["loginId"]
        self.form["password"] = requestForm["password"]

    def form_to_model(self, obj):
        obj.loginId = self.form["loginId"]
        obj.password = self.form["password"]
        return obj

    def display(self, request):
        return render(request, self.get_template())

    def submit(self, request):
        self.request_to_form(request.POST)
        user = self.get_service().authenticate(self.form)
        if (user is None):
            msg = "Invalid ID or Password"
            return render(request, self.get_template(), {"msg": msg})
        else:
            request.session["user"] = user
            return redirect('/ORS/Welcome')

    def signUp(self, request):
        return redirect('/ORS/User')

    def get_service(self):
        return UserService()

    def get_template(self):
        return "LoginView.html"
