from flask import render_template

from .base_ctl import BaseCtl


class WelcomeCtl(BaseCtl):

    def display(self, request, params={}):
        return render_template(self.get_template(), form=self.form)

    def submit(self, request, params={}):
        return render_template(self.get_template(), form=self.form)

    def get_service(self):
        pass

    def get_template(self):
        return 'welcome.html'
