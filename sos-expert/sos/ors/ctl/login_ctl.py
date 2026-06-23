from django.shortcuts import render, redirect

from ..service.user_service import UserService
from ..utility.data_validator import DataValidator


class LoginCtl:

    def __init__(self):
        self.form = {}
        self.form['id'] = 0
        self.form['message'] = ''
        self.form['error'] = False
        self.form['input_error'] = {}

    def request_to_form(self, request):
        self.form['login_id'] = request.POST.get('loginId')
        self.form['password'] = request.POST.get('password')

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False
        if (DataValidator.is_null(request.POST.get("loginId", ''))):
            input_error['login_id'] = 'Login ID is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("password", ''))):
            input_error['password'] = 'Password is required'
            input_error['error'] = True
        return input_error['error']

    def display(self, request, operation='', id=0):
        return render(request, 'login.html', {'form': self.form})

    def submit(self, request):
        operation = request.POST.get('operation', '')

        if operation == "signIn":
            self.request_to_form(request)

            if self.input_validation(request):
                return render(request, 'login.html', {'form': self.form})

            user_data = UserService().authenticate(self.form['login_id'], self.form['password'])

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

            return render(request, 'login.html', {'form': self.form})

        if operation == "signUp":
            return redirect('/ors/Registration/')
