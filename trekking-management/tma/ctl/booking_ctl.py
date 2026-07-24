from flask import render_template, session
from datetime import datetime, date
from .base_ctl import BaseCtl
from ..models import Booking
from ..service.booking_service import BookingService
from ..service.user_service import UserService
from ..service.trek_service import TrekService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility

class BookingCtl(BaseCtl):

    def preload(self, request):
        user_list = UserService().search({})
        trek_list = TrekService().search({})
        booking_status_list = ["Booked", "Cancelled", "Completed"]
        payment_status_list = ["Pending", "Paid"]

        self.preload_data["user_select"] = HtmlUtility.get_list_from_beans(
            "userId",
            int(self.form.get("user_id") or 0),
            user_list
        )

        self.preload_data["trek_select"] = HtmlUtility.get_list_from_beans(
            "trekId",
            int(self.form.get("trek_id") or 0),
            trek_list
        )

        self.preload_data["booking_status_select"] = HtmlUtility.get_list_from_list(
            "bookingStatus",
            self.form.get("booking_status"),
            booking_status_list
        )

        self.preload_data["payment_status_select"] = HtmlUtility.get_list_from_list(
            "paymentStatus",
            self.form.get("payment_status"),
            payment_status_list
        )

        return self.preload_data

    def input_validation(self, request):
        input_error = self.form["input_error"]
        input_error["error"] = False

        if DataValidator.is_null(self.form["user_id"]):
            input_error["user_id"] = "User is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["trek_id"]):
            input_error["trek_id"] = "Trek is required"
            input_error["error"] = True

        if DataValidator.is_null(self.form["booking_date"]):
            input_error["booking_date"] = "Booking Date is required"
            input_error["error"] = True

        return input_error["error"]

    def request_to_form(self, request):
        self.form["id"] = int(request.form.get("id", 0))
        self.form["user_id"] = request.form.get("userId", "")
        self.form["trek_id"] = request.form.get("trekId", "")
        self.form["booking_date"] = request.form.get("bookingDate", "")
        self.form["booking_status"] = request.form.get("bookingStatus", "Booked")
        self.form["payment_status"] = request.form.get("paymentStatus", "Pending")
        self.form["remarks"] = request.form.get("remarks", "")

    def form_to_model(self, obj):
        obj.id = self.form["id"]
        obj.user_id = int(self.form["user_id"])
        obj.trek_id = int(self.form["trek_id"])
        obj.booking_date = datetime.strptime(
            self.form["booking_date"], "%Y-%m-%d"
        ).date()
        obj.booking_status = self.form["booking_status"]
        obj.payment_status = self.form["payment_status"]
        obj.remarks = self.form["remarks"]

        return obj

    def model_to_form(self, obj):
        self.form["id"] = obj.id
        self.form["user_id"] = obj.user_id
        self.form["trek_id"] = obj.trek_id
        self.form["booking_date"] = obj.booking_date.strftime("%Y-%m-%d")
        self.form["booking_status"] = obj.booking_status
        self.form["payment_status"] = obj.payment_status
        self.form["remarks"] = obj.remarks

    def display(self, request, params={}):
        if params['operation'] == 'create' and params['id'] > 0:
            trek = TrekService().get(params['id'])

            if trek:
                self.form["user_id"] = session.get("user_id")
                self.form["trek_id"] = trek.id
                self.form["booking_date"] = date.today().strftime("%Y-%m-%d")
                self.form["booking_status"] = "Booked"
                self.form["payment_status"] = "Pending"

        return render_template(
            self.get_template(),
            form=self.form,
            preload_data=self.preload(request)
        )

    def submit(self, request, params={}):
        try:
            booking = self.form_to_model(Booking())
            self.get_service().save(booking)

            if self.form["id"] > 0:
                self.form["message"] = "Booking Updated Successfully...!!!"
            else:
                self.form["message"] = "Booking Added Successfully...!!!"

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
        return BookingService()

    def get_template(self):
        return "booking.html"