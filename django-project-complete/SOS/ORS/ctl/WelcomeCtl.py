from django.http import HttpResponse
from django.shortcuts import render
from .BaseCtl import BaseCtl


class WelcomeCtl(BaseCtl):
    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def get_template(self):
        return "Welcome.html"

    def get_service(self):
        return "RoleService()"
