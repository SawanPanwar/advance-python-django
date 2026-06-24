from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import User
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator


class UserListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['first_name'] = request.POST.get('firstName')

    def display(self, request, params={}):
        if params['operation'] == 'delete' and params['id'] > 0:
            self.get_service().delete(params['id'])
            return redirect('/ors/UserList/')

        user_list = self.get_service().search(self.form)
        self.form['list'] = user_list
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):

        if request.POST.get('operation', '') == "next":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] += 1
        if request.POST.get('operation', '') == "previous":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] -= 1
        if request.POST.get('operation', '') == "search":
            self.form['page_no'] = 1

        user_list = self.get_service().search(self.form)
        self.form['list'] = user_list
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return UserService()

    def get_template(self):
        return 'userlist.html'
