from flask import render_template

from .base_ctl import BaseCtl
from ..service.booking_service import BookingService
from ..service.dashboard_service import DashboardService


class AdminDashboardCtl(BaseCtl):

    def display(self, request, params={}):
        dashboard_data = self.get_service().get_admin_dashboard()

        self.form.update(dashboard_data)

        self.page_list = BookingService().search(self.form)

        return render_template(
            self.get_template(),
            form=self.form,
            page_list=self.page_list
        )

    def submit(self, request, params={}):
        return render_template(
            self.get_template(),
            form=self.form
        )

    def get_service(self):
        return DashboardService()

    def get_template(self):
        return "admin_dashboard.html"
