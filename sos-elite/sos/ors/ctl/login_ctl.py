from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator


class LoginCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['login_id'] = request.POST.get('loginId')
        self.form['password'] = request.POST.get('password')

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        operation = request.POST.get('operation', '')

        if operation == "signUp":
            return input_error['error']

        if (DataValidator.is_null(request.POST.get("loginId", ''))):
            input_error['login_id'] = 'Login ID is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("password", ''))):
            input_error['password'] = 'Password is required'
            input_error['error'] = True
        return input_error['error']

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        operation = request.POST.get('operation', '')

        if operation == "signIn":
            user_data = self.get_service().authenticate(self.form['login_id'], self.form['password'])

            if user_data:
                request.session['first_name'] = user_data.first_name
                uri = request.POST.get('uri')
                if uri != '':
                    return redirect(uri)
                else:
                    return redirect('/ors/Welcome/')
            else:
                self.form['message'] = 'Login ID & Password Invalid'
                self.form['error'] = True

            return render(request, self.get_template(), {'form': self.form})

        if operation == "signUp":
            return redirect('/ors/Registration/')

    def get_service(self):
        return UserService()

    def get_template(self):
        return 'login.html'
