from flask import Blueprint, render_template, redirect, request, Response

from .ctl.registration_ctl import RegistrationCtl
from .ctl.login_ctl import LoginCtl
from .ctl.welcome_ctl import WelcomeCtl

main_bp = Blueprint(
    "main",
    __name__
)


# Django welcome()
@main_bp.route("/")
def welcome():
    return render_template("welcome.html")


# Django logout()
@main_bp.route("/logout/")
def user_logout():
    from flask import session
    session.clear()
    return redirect("/Login/")


# Controller Mapping
controller_map = {
    "Registration": RegistrationCtl,
    "Welcome": WelcomeCtl,
    "Login": LoginCtl
}


# Django action()
@main_bp.route("/<page>/", methods=["GET", "POST"])
def action(page):
    if page == "favicon.ico":
        return Response(status=204)

    ctl_class = controller_map.get(page)

    if ctl_class is None:
        return "Page Not Found"

    ctl_obj = ctl_class()

    return ctl_obj.execute(operation="", id=0)


# Django action_operation_id()
@main_bp.route("/<page>/<operation>/<int:id>/", methods=["GET", "POST"])
def action_operation_id(page, operation, id):
    ctl_class = controller_map.get(page)

    if ctl_class is None:
        return "Page Not Found"

    ctl_obj = ctl_class()

    return ctl_obj.execute(operation=operation, id=id)
