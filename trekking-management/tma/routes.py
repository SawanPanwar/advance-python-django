from flask import Blueprint, render_template, redirect, request, session, Response

from .ctl.welcome_ctl import WelcomeCtl
from .ctl.user_ctl import UserCtl

main_bp = Blueprint("main", __name__)

controller_map = {
    "Welcome": WelcomeCtl,
    "User": UserCtl,
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
