from django.shortcuts import render, redirect

from ..models import User
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator


class UserListCtl:

    def __init__(self):
        self.form = {}
        self.form['id'] = 0
        self.form['message'] = ''
        self.form['error'] = False
        self.form['input_error'] = {}
        self.form['page_no'] = 1
        self.form['page_size'] = 5
        self.form['list'] = []

    def request_to_form(self, request):
        self.form['first_name'] = request.POST.get('firstName')

    def display(self, request, operation='', id=0):
        if operation == 'delete':
            UserService().delete(id)
            return redirect('/ors/UserList/')

        user_list = UserService().search(self.form)
        self.form['list'] = user_list
        return render(request, "userlist.html", {"form": self.form})

    def submit(self, request):

        self.request_to_form(request)

        if request.POST.get('operation', '') == "next":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] += 1
        if request.POST.get('operation', '') == "previous":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] -= 1
        if request.POST.get('operation', '') == "search":
            self.form['page_no'] = 1

        user_list = UserService().search(self.form)
        self.form['list'] = user_list

        return render(request, "userlist.html", {"form": self.form})
