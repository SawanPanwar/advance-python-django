from .BaseCtl import BaseCtl
from django.shortcuts import render, redirect
from ..utility.DataValidator import DataValidator
from ..service.UserService import UserService


class LoginCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form["loginId"] = requestForm["loginId"]
        self.form["password"] = requestForm["password"]

    def input_validation(self):
        super().input_validation()

        inputError = self.form["inputError"]
        if (DataValidator.isNull(self.form["loginId"])):
            inputError["loginId"] = "Login ID is required"
            self.form["error"] = True
        else:
            if (DataValidator.isemail(self.form['loginId'])):
                inputError['loginId'] = "Login Id must be email"
                self.form['error'] = True

        if (DataValidator.isNull(self.form["password"])):
            inputError["password"] = "Password is required"
            self.form["error"] = True

        return self.form["error"]

    def display(self, request, params={}):
        self.form['out'] = params.get("out")
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        PATH = params.get('path')
        user = self.get_service().authenticate(self.form)
        if (user is None):
            self.form['error'] = True
            self.form["messege"] = "Login ID & Password is Invalid"
            res = render(request, self.get_template(), {"form": self.form})
        else:
            request.session["user"] = user
            request.session['name'] = user.roleName
            res = redirect('/ORS/Welcome/')
        return res

    def get_template(self):
        return "Login.html"

    def get_service(self):
        return UserService()
