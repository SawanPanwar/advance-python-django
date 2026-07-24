from flask import render_template

from .base_ctl import BaseCtl
from ..models import Trek
from ..service.trek_service import TrekService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class TrekCtl(BaseCtl):

    def preload(self, request):

        difficulty_list = ["Easy", "Moderate", "Hard"]

        status_list = ["Pending", "Approved", "Open", "Closed", "Completed"]

        self.preload_data["difficulty_select"] = HtmlUtility.get_list_from_list(
            "difficulty",
            self.form.get("difficulty"),
            difficulty_list
        )

        self.preload_data["status_select"] = HtmlUtility.get_list_from_list(
            "status",
            self.form.get("status"),
            status_list
        )

        return self.preload_data

    def input_validation(self, request):

        input_error = self.form.get("input_error")
        input_error["error"] = False

        if DataValidator.is_null(self.form["trek_name"]):
            input_error["trek_name"] = "Trek Name is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["location"]):
            input_error["location"] = "Location is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form['difficulty']) or request.form.get("difficulty") == "0":
            input_error["difficulty"] = "Difficulty is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["duration"]):
            input_error["duration"] = "Duration is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["total_slots"]):
            input_error["total_slots"] = "Total Slots is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["available_slots"]):
            input_error["available_slots"] = "Available Slots is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["price"]):
            input_error["price"] = "Price is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["description"]):
            input_error["description"] = "Description is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["start_date"]):
            input_error["start_date"] = "Start Date is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["end_date"]):
            input_error["end_date"] = "End Date is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form['status']) or request.form.get("status") == "0":
            input_error['status'] = 'Status is required'
            input_error['error'] = True

        return input_error["error"]

    def request_to_form(self, request):

        self.form["id"] = int(request.form.get("id", 0))
        self.form["trek_name"] = request.form.get("trekName", "")
        self.form["location"] = request.form.get("location", "")
        self.form["difficulty"] = request.form.get("difficulty", "")
        self.form["duration"] = request.form.get("duration", "")
        self.form["total_slots"] = request.form.get("totalSlots", "")
        self.form["available_slots"] = request.form.get("availableSlots", "")
        self.form["price"] = request.form.get("price", "")
        self.form["description"] = request.form.get("description", "")
        self.form["start_date"] = request.form.get("startDate", "")
        self.form["end_date"] = request.form.get("endDate", "")
        self.form["status"] = request.form.get("status", "")

    def form_to_model(self, obj):

        obj.id = self.form["id"]
        obj.trek_name = self.form["trek_name"]
        obj.location = self.form["location"]
        obj.difficulty = self.form["difficulty"]
        obj.duration = int(self.form["duration"])
        obj.total_slots = int(self.form["total_slots"])
        obj.available_slots = int(self.form["available_slots"])
        obj.price = float(self.form["price"])
        obj.description = self.form["description"]
        obj.start_date = self.form["start_date"]
        obj.end_date = self.form["end_date"]
        obj.status = self.form["status"]

        return obj

    def model_to_form(self, obj):

        self.form["id"] = obj.id
        self.form["trek_name"] = obj.trek_name
        self.form["location"] = obj.location
        self.form["difficulty"] = obj.difficulty
        self.form["duration"] = obj.duration
        self.form["total_slots"] = obj.total_slots
        self.form["available_slots"] = obj.available_slots
        self.form["price"] = obj.price
        self.form["description"] = obj.description
        self.form["start_date"] = obj.start_date
        self.form["end_date"] = obj.end_date
        self.form["status"] = obj.status

    def display(self, request, params={}):

        return render_template(
            self.get_template(),
            form=self.form,
            preload_data=self.preload(request)
        )

    def submit(self, request, params={}):

        try:

            trek = self.form_to_model(Trek())

            self.get_service().save(trek)

            if self.form["id"] > 0:
                self.form["message"] = "Trek Updated Successfully...!!!"
            else:
                self.form["message"] = "Trek Added Successfully...!!!"

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
        return TrekService()

    def get_template(self):
        return "trek.html"
