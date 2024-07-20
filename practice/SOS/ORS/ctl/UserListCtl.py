from ..service.UserService import UserService
from django.shortcuts import render, redirect
from .BaseCtl import BaseCtl


class UserListCtl(BaseCtl):
    count = 1

    def __init__(self):
        self.form = {}
        self.form["pageNo"] = 1

    def request_to_form(self, requestForm):
        self.form['firstName'] = requestForm.get("firstName", None)
        self.form['ids'] = requestForm.getlist('ids', None)

    def preload(self, request):
        self.page_list = self.get_service().preload()
        self.preload_data = self.page_list

    def display(self, request):
        record = self.get_service().search(self.form)
        data = record['data']
        return render(request, self.get_template(), {"list": data, 'form': self.form, 'preList':self.preload_data})

    def submit(self, request):
        self.form['firstName'] = request.POST["firstName"]
        self.form['lastName'] = request.POST["lastName"]
        self.form['id'] = request.POST["userId"]
        record = self.get_service().search(self.form)
        data = record['data']
        return render(request, self.get_template(), {"list": data, 'form': self.form, 'preList':self.preload_data})

    def next(self, request):
        UserListCtl.count += 1
        self.form['pageNo'] = UserListCtl.count
        return self.submit(request)

    def previous(self, request):
        UserListCtl.count -= 1
        self.form['pageNo'] = UserListCtl.count
        return self.submit(request)

    def delete(self, request):
        recordList = request.POST.getlist('ids', None)
        for ids in recordList:
            id = int(ids)
            if (id > 0):
                r = self.get_service().get(id)
                UserService().delete(r)
        return self.submit(request)

    def add(self, request):
        return redirect('/ORS/User')

    def get_service(self):
        return UserService()

    def get_template(self):
        return "UserList.html"
