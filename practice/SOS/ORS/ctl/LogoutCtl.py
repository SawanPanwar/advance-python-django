from django.shortcuts import render, redirect
from .BaseCtl import BaseCtl

class LogoutCtl(BaseCtl):
    def display(self, request):
        request.session['user'] = None
        return redirect('/ORS/Login')
    def submit(self, request):
        pass
    def get_service(self):
        pass
    def get_template(self):
        return "LoginView.html"
