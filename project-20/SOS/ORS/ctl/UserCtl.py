from django.shortcuts import render, redirect
from ..utility.DataValidator import DataValidator
from ..utility.HtmlUtility import HTMLUtility
from django.http import HttpResponse
from .BaseCtl import BaseCtl
from ..models import User
from ..service.UserService import UserService
from ..service.RoleService import RoleService


class UserCtl(BaseCtl):

    def preload(self, request):
        self.page_list = RoleService().preload()
        # self.preloadData = self.page_list
        self.form["roleId"] = request.POST.get('roleId', 0)
        self.dynamic_preload = HTMLUtility.get_list_from_objects('roleId', self.form["roleId"], self.page_list)

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form["firstName"] = requestForm["firstName"]
        self.form["lastName"] = requestForm["lastName"]
        self.form["loginId"] = requestForm["loginId"]
        self.form["password"] = requestForm["password"]
        self.form["confirmPassword"] = requestForm["confirmPassword"]
        self.form["dob"] = requestForm["dob"]
        self.form["address"] = requestForm["address"]
        self.form["gender"] = requestForm["gender"]
        self.form["mobileNumber"] = requestForm["mobileNumber"]
        self.form["roleId"] = requestForm["roleId"]

    def form_to_model(self, obj):
        c = RoleService().get(self.form['roleId'])
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.firstName = self.form["firstName"]
        obj.lastName = self.form["lastName"]
        obj.loginId = self.form["loginId"]
        obj.password = self.form["password"]
        obj.confirmPassword = self.form["confirmPassword"]
        obj.dob = self.form["dob"]
        obj.address = self.form["address"]
        obj.gender = self.form["gender"]
        obj.mobileNumber = self.form["mobileNumber"]
        obj.roleId = self.form["roleId"]
        obj.roleName = c.name
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form["id"] = obj.id
        self.form["firstName"] = obj.firstName
        self.form["lastName"] = obj.lastName
        self.form["loginId"] = obj.loginId
        self.form["password"] = obj.password
        self.form["confirmPassword"] = obj.confirmPassword
        self.form["dob"] = obj.dob.strftime("%Y-%m-%d")
        self.form["address"] = obj.address
        self.form["gender"] = obj.gender
        self.form["mobileNumber"] = obj.mobileNumber
        self.form["roleId"] = obj.roleId
        self.form["roleName"] = obj.roleName

    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]

        if (DataValidator.isNull(self.form["firstName"])):
            inputError["firstName"] = "First Name is required"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["lastName"])):
            inputError["lastName"] = "Last Name is required"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["loginId"])):
            inputError["loginId"] = "Login ID is required"
            self.form["error"] = True
        else:
            if (DataValidator.isemail(self.form['loginId'])):
                inputError['loginId'] = "Login ID must be like student@gmail.com"
                self.form['error'] = True

        if (DataValidator.isNull(self.form["password"])):
            inputError["password"] = "Password is required"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["confirmPassword"])):
            inputError["confirmPassword"] = "Confirm Password is required"
            self.form["error"] = True

        if (DataValidator.isNotNull(self.form['confirmPassword'])):
            if (self.form['password'] != self.form['confirmPassword']):
                inputError['confirmPassword'] = "Password & Confirm Password are not same"
                self.form["error"] = True

        if (DataValidator.isNull(self.form["dob"])):
            inputError["dob"] = "DOB is required"
            self.form["error"] = True
        else:
            if (DataValidator.isDate(self.form['dob'])):
                inputError['dob'] = "Incorrect Date, should be YYYY-MM-DD"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['gender'])):
            inputError['gender'] = "Gender is required"
            self.form['error'] = True

        if (DataValidator.isNull(self.form["address"])):
            inputError["address"] = "Address is required"
            self.form["error"] = True

        if (DataValidator.isNull(self.form["mobileNumber"])):
            inputError["mobileNumber"] = "Mobile Number is required"
            self.form["error"] = True
        else:
            if (DataValidator.ismobilecheck(self.form['mobileNumber'])):
                inputError['mobileNumber'] = "Mobile No should start with 6,7,8,9"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['roleId'])):
            inputError['roleId'] = "Role Name is required"
            self.form['error'] = True
        return self.form['error']

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form, 'role_preload': self.dynamic_preload})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(User())
        self.get_service().save(r)
        self.form['error'] = False
        self.form['messege'] = "User Added successfully..!!"
        res = render(request, self.get_template(), {'form': self.form, 'role_preload': self.dynamic_preload})
        return res

    def get_template(self):
        return "User.html"

    def get_service(self):
        return UserService()
