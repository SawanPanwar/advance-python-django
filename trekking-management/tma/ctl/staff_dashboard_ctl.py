from flask import render_template, session

from .base_ctl import BaseCtl
from ..service.dashboard_service import DashboardService


class StaffDashboardCtl(BaseCtl):

    def display(self, request, params={}):

        staff_id = session.get("user_id")

        dashboard_data = self.get_service().get_staff_dashboard(
            staff_id
        )

        self.form.update(dashboard_data)

        return render_template(
            self.get_template(),
            form=self.form
        )


    def submit(self, request, params={}):

        return render_template(
            self.get_template(),
            form=self.form
        )


    def get_service(self):
        return DashboardService()


    def get_template(self):
        return "staff_dashboard.html"