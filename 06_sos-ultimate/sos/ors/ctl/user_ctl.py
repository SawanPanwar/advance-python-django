from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import User
from ..service.role_service import RoleService
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class UserCtl(BaseCtl):

    def preload(self, request):
        gender_list = ["Male", "Female"]
        role_list = RoleService().search({})

        self.form["preload_data"]["gender_select"] = HtmlUtility.get_list_from_list(
            "gender",
            self.form.get("gender"),
            gender_list
        )

        self.form["preload_data"]["role_select"] = HtmlUtility.get_list_from_beans(
            "roleId",
            int(self.form.get("role_id") or 0),
            role_list
        )

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(self.form['first_name'])):
            input_error['first_name'] = 'First Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['last_name'])):
            input_error['last_name'] = 'Last Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['login_id'])):
            input_error['login_id'] = 'Login ID is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['password'])):
            input_error['password'] = 'Password is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['dob'])):
            input_error['dob'] = 'DOB is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['address'])):
            input_error['address'] = 'Address is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['gender']) or request.POST.get("gender") == "0"):
            input_error['gender'] = 'Gender is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['role_id']) or request.POST.get("roleId") == "0"):
            input_error['role_id'] = 'Role is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['first_name'] = request.POST.get('firstName', '')
        self.form['last_name'] = request.POST.get('lastName', '')
        self.form['login_id'] = request.POST.get('loginId', '')
        self.form['password'] = request.POST.get('password', '')
        self.form['dob'] = request.POST.get('dob', '')
        self.form['address'] = request.POST.get('address', '')
        self.form['gender'] = request.POST.get('gender', '')
        self.form['role_id'] = request.POST.get('roleId', 0)

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.first_name = self.form['first_name']
        obj.last_name = self.form['last_name']
        obj.login_id = self.form['login_id']
        obj.password = self.form['password']
        obj.dob = self.form['dob']
        obj.address = self.form['address']
        obj.gender = self.form['gender']
        obj.role_id = int(self.form['role_id'])
        obj.role_name = RoleService().get(self.form['role_id']).name
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['first_name'] = obj.first_name
        self.form['last_name'] = obj.last_name
        self.form['login_id'] = obj.login_id
        self.form['password'] = obj.password
        self.form['dob'] = obj.dob.strftime('%Y-%m-%d')
        self.form['address'] = obj.address
        self.form['gender'] = obj.gender
        self.form['role_id'] = obj.role_id
        self.form['role_name'] = obj.role_name

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form,  "preload_data": self.preload(request)})

    def submit(self, request, params={}):
        try:
            user = self.form_to_model(User())
            self.get_service().save(user)
            if self.form['id'] > 0:
                self.form['message'] = 'User Updated Successfully...!!!'
            else:
                self.form['message'] = 'User Added Successfully...!!!'
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True
        return render(request, self.get_template(), {'form': self.form,  "preload_data": self.preload(request)})

    def get_service(self):
        return UserService()

    def get_template(self):
        return 'user.html'
