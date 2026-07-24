from datetime import date

from flask import render_template, session

from .base_ctl import BaseCtl
from ..models import StaffAssignment
from ..service.staff_assignment_service import StaffAssignmentService
from ..service.trek_service import TrekService
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class StaffAssignmentCtl(BaseCtl):

    def preload(self, request):

        trek_list = TrekService().search({})
        staff_list = UserService().search({})  # Approved Staff list

        self.preload_data["trek_select"] = HtmlUtility.get_list_from_beans(
            "trek_id",
            self.form.get("trek_id"),
            trek_list
        )

        self.preload_data["staff_select"] = HtmlUtility.get_list_from_beans(
            "staff_id",
            self.form.get("staff_id"),
            staff_list
        )

        status_list = ["Assigned", "Completed", "Cancelled"]

        self.preload_data["status_select"] = HtmlUtility.get_list_from_list(
            "status",
            self.form.get("status"),
            status_list
        )

        return self.preload_data

    def input_validation(self, request):

        input_error = self.form.get("input_error")
        input_error["error"] = False

        if self.form["trek_id"] == "0":
            input_error["trek_id"] = "Trek is required"
            input_error["error"] = True

        if self.form["staff_id"] == "0":
            input_error["staff_id"] = "Staff is required"
            input_error["error"] = True

        return input_error["error"]

    def request_to_form(self, request):

        self.form["id"] = int(request.form.get("id", 0))
        self.form["trek_id"] = request.form.get("trek_id", "")
        self.form["staff_id"] = request.form.get("staff_id", "")
        self.form["assigned_date"] = request.form.get("assignedDate", "")
        self.form["status"] = request.form.get("status", "")

    def form_to_model(self, obj):

        obj.id = self.form["id"]

        obj.trek_id = int(self.form["trek_id"])
        obj.staff_id = int(self.form["staff_id"])

        trek = TrekService().get(obj.trek_id)
        obj.trek_name = trek.trek_name

        staff = UserService().get(obj.staff_id)
        obj.staff_name = staff.first_name + " " + staff.last_name

        obj.assigned_date = date.today()
        obj.status = self.form["status"]

        return obj

    def model_to_form(self, obj):

        self.form["id"] = obj.id
        self.form["trek_id"] = obj.trek_id
        self.form["staff_id"] = obj.staff_id
        self.form["assigned_date"] = obj.assigned_date.strftime("%Y-%m-%d")
        self.form["status"] = obj.status

    def display(self, request, params={}):

        if params['operation'] == 'create' and params['id'] > 0:
            trek = TrekService().get(params['id'])

            if trek:
                self.form["trek_id"] = trek.id
                self.form["assigned_date"] = date.today().strftime("%Y-%m-%d")
                self.form["status"] = "Assigned"

        return render_template(
            self.get_template(),
            form=self.form,
            preload_data=self.preload(request)
        )

    def submit(self, request, params={}):

        try:

            assignment = self.form_to_model(StaffAssignment())

            self.get_service().save(assignment)

            if self.form["id"] > 0:
                self.form["message"] = "Staff Assignment Updated Successfully...!!!"
            else:
                self.form["message"] = "Staff Assigned Successfully...!!!"

            self.form["error"] = False

        except Exception as e:

            self.form["message"] = str(e)
            self.form["error"] = True

        return render_template(
            self.get_template(),
            form=self.form,
            preload_data=self.preload(request)
        )

    def get_service(self):
        return StaffAssignmentService()

    def get_template(self):
        return "staffassignment.html"
