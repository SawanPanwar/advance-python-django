from flask import render_template, redirect, session

from .base_ctl import BaseCtl
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator


class LoginCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['login_id'] = request.form.get('loginId')
        self.form['password'] = request.form.get('password')

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if DataValidator.is_null(request.form.get("loginId", '')):
            input_error['login_id'] = 'Login ID is required'
            input_error['error'] = True

        if DataValidator.is_null(request.form.get("password", '')):
            input_error['password'] = 'Password is required'
            input_error['error'] = True

        return input_error['error']

    def display(self, request, params={}):
        return render_template(self.get_template(), form=self.form)

    def submit(self, request, params={}):
        operation = request.form.get('operation', '')

        if operation == "signIn":

            user_data = self.get_service().authenticate(self.form['login_id'], self.form['password'])

            if user_data:

                session['first_name'] = user_data.first_name

                uri = request.form.get('uri')

                if uri != '':
                    return redirect(uri)
                else:
                    return redirect('/Welcome/')

            else:
                self.form['message'] = 'Login ID & Password Invalid'
                self.form['error'] = True

        return render_template(self.get_template(), form=self.form)

    def get_service(self):
        return UserService()

    def get_template(self):
        return 'login.html'
