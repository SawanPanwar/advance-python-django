from django.shortcuts import render, redirect

from ..models import User
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator


class UserCtl:

    def __init__(self):
        self.form = {}
        self.form['id'] = 0
        self.form['message'] = ''
        self.form['error'] = False
        self.form['input_error'] = {}

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False
        if (DataValidator.is_null(request.POST.get("firstName", ''))):
            input_error['first_name'] = 'First Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("lastName", ''))):
            input_error['last_name'] = 'Last Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("loginId", ''))):
            input_error['login_id'] = 'Login ID is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("password", ''))):
            input_error['password'] = 'Password is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("dob", ''))):
            input_error['dob'] = 'DOB is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("address", ''))):
            input_error['address'] = 'Address is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['first_name'] = request.POST.get('firstName')
        self.form['last_name'] = request.POST.get('lastName')
        self.form['login_id'] = request.POST.get('loginId')
        self.form['password'] = request.POST.get('password')
        self.form['dob'] = request.POST.get('dob')
        self.form['address'] = request.POST.get('address')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.first_name = self.form['first_name']
        obj.last_name = self.form['last_name']
        obj.login_id = self.form['login_id']
        obj.password = self.form['password']
        obj.dob = self.form['dob']
        obj.address = self.form['address']
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['first_name'] = obj.first_name
        self.form['last_name'] = obj.last_name
        self.form['login_id'] = obj.login_id
        self.form['password'] = obj.password
        self.form['dob'] = obj.dob.strftime('%Y-%m-%d')
        self.form['address'] = obj.address

    def display(self, request, operation='', id=0):
        if operation == 'edit' and id > 0:
            user = UserService().get(id)
            self.model_to_form(user)
        return render(request, 'user.html', {'form': self.form})

    def submit(self, request):

        operation = request.POST.get('operation', '')

        if operation == 'save':
            self.request_to_form(request)

            if self.input_validation(request):
                return render(request, 'user.html', {'form': self.form})

            try:
                user = self.form_to_model(User())
                UserService().save(user)
                self.form['message'] = 'User Added Successfully...!!!'
            except Exception as e:
                self.form['message'] = str(e)
                self.form['error'] = True

            return render(request, 'user.html', {'form': self.form})

        elif operation == 'update':
            self.request_to_form(request)

            if self.input_validation(request):
                return render(request, 'user.html', {'form': self.form})

            try:
                user = self.form_to_model(User())
                UserService().save(user)
                self.form['message'] = 'User Updated Successfully...!!!'
            except Exception as e:
                self.form['message'] = str(e)
                self.form['error'] = True

            return render(request, 'user.html', {'form': self.form})

        elif operation == "reset":
            return redirect('/ors/User/')

        elif operation == "list":
            return redirect('/ors/UserList/')
