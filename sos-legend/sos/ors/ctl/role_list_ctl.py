from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..service.role_service import RoleService


class RoleListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['name'] = request.POST.get('name')

    def display(self, request, params={}):
        role_list = self.get_service().search(self.form)
        self.form['list'] = role_list
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

        role_list = RoleService().search(self.form)
        self.form['list'] = role_list

        return render(request, "rolelist.html", {"form": self.form})

    def get_service(self):
        return RoleService()

    def get_template(self):
        return 'rolelist.html'
