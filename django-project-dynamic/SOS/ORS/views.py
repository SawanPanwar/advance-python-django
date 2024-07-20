import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MarksheetForm
from .models import Marksheet

logger = logging.getLogger(__name__)


def user_signup(request):
    message = ''
    if request.method == "POST":
        userName = request.POST["userName"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        obj = User.objects.create_superuser(userName, email, password)
        obj.first_name = firstName
        obj.last_name = lastName
        obj.save()
        message = 'User Registered Successfully'
    return render(request, "UserRegistration.html", {'message': message})


def user_signin(request):
    message = ''
    if request.method == "POST":
        userName = request.POST["userName"]
        password = request.POST["password"]
        user = authenticate(username=userName, password=password)
        if user is not None:
            request.session["userName"] = userName
            login(request, user)
            return redirect("WELCOME")
        else:
            message = 'Invalid User'
    return render(request, "Login.html", {'message': message})


def welcome(request):
    return render(request, "Welcome.html", )


def user_logout(request):
    logout(request)
    return redirect("SIGN_IN")


@login_required()
def add_marksheet(request):
    message = ''
    form = MarksheetForm()
    if request.method == "POST":
        form = MarksheetForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Marksheet Added Successfully'
    return render(request, "Marksheet.html", {'message': message})


@login_required()
def marksheet_list(request):
    list = Marksheet.objects.all()
    return render(request, "MarksheetList.html", {"list": list})


@login_required()
def edit_marksheet(request, id):
    message = ''
    obj = Marksheet.objects.get(id=id)
    if request.method == "POST":
        form = MarksheetForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            message = 'Marksheet Updated Successfully'
    return render(request, "Marksheet.html", {"form": obj, "id": id, 'message': message})


@login_required()
def delete_marksheet(request, id):
    obj = Marksheet.objects.get(id=id)
    obj.delete()
    return redirect("/ORS/list")


def test_logging(request):
    try:
        c = 10 / 0
    except Exception as e:
        logger.info(e)

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.fatal("fatal message")
    return HttpResponse('<h1>Logger Works..!!!</h1>');
