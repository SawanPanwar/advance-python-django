from flask import Blueprint, render_template, redirect, request, session, Response

from .ctl.admin_dashboard_ctl import AdminDashboardCtl
from .ctl.booking_list_ctl import BookingListCtl
from .ctl.staff_dashboard_ctl import StaffDashboardCtl
from .ctl.user_dashboard_ctl import UserDashboardCtl
from .ctl.welcome_ctl import WelcomeCtl
from .ctl.trek_ctl import TrekCtl
from .ctl.registration_ctl import RegistrationCtl
from .ctl.login_ctl import LoginCtl
from .ctl.dashboard_ctl import DashboardCtl
from .ctl.trek_list_ctl import TrekListCtl
from .ctl.user_list_ctl import UserListCtl
from .ctl.user_ctl import UserCtl
from .ctl.booking_ctl import BookingCtl
from .ctl.staff_assignment_ctl import StaffAssignmentCtl
from .ctl.staff_assignment_list_ctl import StaffAssignmentListCtl

main_bp = Blueprint("main", __name__)

controller_map = {
    "Welcome": WelcomeCtl,
    "Trek": TrekCtl,
    "TrekList": TrekListCtl,
    "Login": LoginCtl,
    "Registration": RegistrationCtl,
    "Dashboard": DashboardCtl,
    "UserList": UserListCtl,
    "User": UserCtl,
    "Booking": BookingCtl,
    "BookingList": BookingListCtl,
    "StaffAssignment": StaffAssignmentCtl,
    "StaffAssignmentList": StaffAssignmentListCtl,

    "AdminDashboard": AdminDashboardCtl,
    "StaffDashboard": StaffDashboardCtl,
    "UserDashboard": UserDashboardCtl,
}


@main_bp.route("/")
def welcome():
    return render_template("welcome.html")


@main_bp.route("/logout/")
def user_logout():
    session.clear()
    return redirect("/Login/")


@main_bp.route("/<page>/", methods=["GET", "POST"])
def action(page):
    if "favicon.ico" in request.path:
        return Response(status=204)

    ctl_class = controller_map.get(page)

    if ctl_class is None:
        return "Page Not Found", 404

    ctl_obj = ctl_class()

    return ctl_obj.execute(request, params={"operation": "", "id": 0})


@main_bp.route("/<page>/<operation>/<int:id>/", methods=["GET", "POST"])
def action_operation_id(page, operation="", id=0):
    if "favicon.ico" in request.path:
        return Response(status=204)

    ctl_class = controller_map.get(page)

    if ctl_class is None:
        return "Page Not Found", 404

    ctl_obj = ctl_class()

    return ctl_obj.execute(request, params={"operation": operation, "id": id})
