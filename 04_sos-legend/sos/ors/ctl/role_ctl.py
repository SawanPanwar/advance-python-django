from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import Role
from ..service.role_service import RoleService
from ..utility.data_validator import DataValidator


class RoleCtl(BaseCtl):

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(request.POST.get("name", ''))):
            input_error['name'] = 'Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("description", ''))):
            input_error['description'] = 'Description is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['name'] = request.POST.get('name')
        self.form['description'] = request.POST.get('description')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.name = self.form['name']
        obj.description = self.form['description']
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['description'] = obj.description

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        try:
            role = self.form_to_model(Role())
            self.get_service().save(role)
            if self.form['id'] > 0:
                self.form['message'] = 'Role Updated Successfully...!!!'
            else:
                self.form['message'] = 'Role Added Successfully...!!!'
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return RoleService()

    def get_template(self):
        return 'role.html'
