from django.shortcuts import render, redirect
from ..models import User
from ..service.UserService import UserService
from .BaseCtl import BaseCtl


class UserCtl(BaseCtl):
    def __init__(self):
        self.form = {}
        self.form["id"] = 0

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form["firstName"] = requestForm["firstName"]
        self.form["lastName"] = requestForm["lastName"]
        self.form["loginId"] = requestForm["loginId"]
        self.form["password"] = requestForm["password"]

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.firstName = self.form["firstName"]
        obj.lastName = self.form["lastName"]
        obj.loginId = self.form["loginId"]
        obj.password = self.form["password"]
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form["id"] = obj.id
        self.form["firstName"] = obj.firstName
        self.form["lastName"] = obj.lastName
        self.form["loginId"] = obj.loginId
        self.form["password"] = obj.password

    def display(self, request):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request):
        self.request_to_form(request.POST)
        s = self.form_to_model(User())
        self.get_service().save(s)
        return render(request, self.get_template(), {'form': self.form})

    def edit(self, request, id=0):
        data = self.get_service().get(int(id))
        self.model_to_form(data)
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return UserService()

    def get_template(self):
        return "Registration.html"
