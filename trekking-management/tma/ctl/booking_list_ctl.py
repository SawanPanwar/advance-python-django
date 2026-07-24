from flask import render_template

from .base_ctl import BaseCtl
from ..service.booking_service import BookingService


class BookingListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form["booking_status"] = request.form.get("bookingStatus", "")
        self.form["payment_status"] = request.form.get("paymentStatus", "")

    def display(self, request, params={}):
        self.page_list = self.get_service().search(self.form)

        return render_template(
            self.get_template(),
            form=self.form,
            page_list=self.page_list
        )

    def submit(self, request, params={}):

        operation = request.form.get("operation", "")

        if operation == "next":
            self.form["page_no"] = int(request.form.get("pageNo", 1))
            self.form["page_no"] += 1

        elif operation == "previous":
            self.form["page_no"] = int(request.form.get("pageNo", 1))
            self.form["page_no"] -= 1

        elif operation == "search":
            self.form["page_no"] = 1

        self.page_list = self.get_service().search(self.form)

        return render_template(
            self.get_template(),
            form=self.form,
            page_list=self.page_list
        )

    def get_service(self):
        return BookingService()

    def get_template(self):
        return "bookinglist.html"