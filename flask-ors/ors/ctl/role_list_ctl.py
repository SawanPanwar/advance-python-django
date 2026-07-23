from flask import render_template

from .base_ctl import BaseCtl
from ..service.role_service import RoleService


class RoleListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['name'] = request.form.get('name')

    def display(self, request, params={}):
        self.page_list = self.get_service().search(self.form)
        return render_template(self.get_template(), form=self.form, page_list=self.page_list)

    def submit(self, request, params={}):

        if request.form.get('operation', '') == "next":
            self.form['page_no'] = int(request.form.get('pageNo'))
            self.form['page_no'] += 1

        if request.form.get('operation', '') == "previous":
            self.form['page_no'] = int(request.form.get('pageNo'))
            self.form['page_no'] -= 1

        if request.form.get('operation', '') == "search":
            self.form['page_no'] = 1

        self.page_list = self.get_service().search(self.form)

        return render_template(self.get_template(), form=self.form, page_list=self.page_list)

    def get_service(self):
        return RoleService()

    def get_template(self):
        return 'rolelist.html'
