from flask import render_template

from .base_ctl import BaseCtl
from ..models import User
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class RegistrationCtl(BaseCtl):

    def preload(self, request):
        gender_list = ["Male", "Female"]

        self.preload_data["gender_select"] = HtmlUtility.get_list_from_list(
            "gender",
            self.form.get("gender"),
            gender_list
        )

        return self.preload_data

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if DataValidator.is_null(request.form.get("firstName", '')):
            input_error['first_name'] = 'First Name is required'
            input_error['error'] = True

        if DataValidator.is_null(request.form.get("lastName", '')):
            input_error['last_name'] = 'Last Name is required'
            input_error['error'] = True

        if DataValidator.is_null(request.form.get("loginId", '')):
            input_error['login_id'] = 'Login ID is required'
            input_error['error'] = True

        if DataValidator.is_null(request.form.get("password", '')):
            input_error['password'] = 'Password is required'
            input_error['error'] = True

        if DataValidator.is_null(request.form.get("dob", '')):
            input_error['dob'] = 'DOB is required'
            input_error['error'] = True

        if DataValidator.is_null(request.form.get("address", '')):
            input_error['address'] = 'Address is required'
            input_error['error'] = True

        if DataValidator.is_null(request.form.get("gender", '')) or request.form.get("gender") == "0":
            input_error['gender'] = 'Gender is required'
            input_error['error'] = True

        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.form.get('id', 0))
        self.form['first_name'] = request.form.get('firstName')
        self.form['last_name'] = request.form.get('lastName')
        self.form['login_id'] = request.form.get('loginId')
        self.form['password'] = request.form.get('password')
        self.form['dob'] = request.form.get('dob')
        self.form['address'] = request.form.get('address')
        self.form['gender'] = request.form.get('gender')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.first_name = self.form['first_name']
        obj.last_name = self.form['last_name']
        obj.login_id = self.form['login_id']
        obj.password = self.form['password']
        obj.dob = self.form['dob']
        obj.address = self.form['address']
        obj.gender = self.form['gender']
        obj.role_id = 2
        obj.role_name = 'Student'

        return obj

    def display(self, request, params={}):
        return render_template(self.get_template(), form=self.form, preload_data=self.preload(request))

    def submit(self, request, params={}):

        try:
            user = self.form_to_model(User())
            self.get_service().save(user)

            self.form['message'] = 'User Registration Successfully...!!!'
            self.form['error'] = False

        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True

        return render_template(self.get_template(), form=self.form, preload_data=self.preload(request))

    def get_service(self):
        return UserService()

    def get_template(self):
        return 'registration.html'
