from flask import render_template, redirect, session

from .base_ctl import BaseCtl
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator


class LoginCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['email'] = request.form.get('email')
        self.form['password'] = request.form.get('password')

    def input_validation(self, request):

        input_error = self.form.get("input_error")
        input_error['error'] = False

        if DataValidator.is_null(request.form.get("email", '')):
            input_error['email'] = 'Email ID is required'
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

            user_data = self.get_service().authenticate(self.form['email'], self.form['password'])

            if user_data:

                # Blacklisted user/staff check
                if user_data.status == "Blacklisted":
                    self.form['message'] = "Your account is blacklisted"
                    self.form['error'] = True

                    return render_template(self.get_template(), form=self.form)

                # ADMIN LOGIN
                if user_data.role == "Admin":

                    if user_data.status == "Active":
                        session['user_id'] = user_data.id
                        session['role'] = user_data.role
                        session['first_name'] = user_data.first_name

                        return redirect('/AdminDashboard/')

                # STAFF LOGIN
                elif user_data.role == "Staff":

                    if user_data.status == "Pending":

                        self.form['message'] = "Admin approval pending"
                        self.form['error'] = True

                    elif user_data.status == "Approved":

                        session['user_id'] = user_data.id
                        session['role'] = user_data.role
                        session['first_name'] = user_data.first_name

                        return redirect('/StaffDashboard/')

                # USER LOGIN
                elif user_data.role == "User":

                    if user_data.status == "Active":
                        session['user_id'] = user_data.id
                        session['role'] = user_data.role
                        session['first_name'] = user_data.first_name

                        return redirect('/UserDashboard/')

            else:

                self.form['message'] = 'Login ID & Password Invalid'
                self.form['error'] = True

        return render_template(self.get_template(), form=self.form)

    def get_service(self):
        return UserService()

    def get_template(self):
        return 'login.html'
