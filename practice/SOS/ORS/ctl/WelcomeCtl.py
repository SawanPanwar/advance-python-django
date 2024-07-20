from django.shortcuts import render, redirect
from .BaseCtl import BaseCtl

class WelcomeCtl(BaseCtl):

    def display(self, request):
        return render(request, self.get_template())

    def submit(self, request):
        pass

    def get_template(self):
        return "Welcome.html"

    def get_service(self):
        pass