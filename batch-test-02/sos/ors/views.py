from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Marksheet


def welcome(request):
    return render(request, 'welcome.html')


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
    return render(request, "registration.html", {'message': message})


def user_signin(request):
    message = ''
    if request.method == "POST":
        if request.POST.get('operation') == "signIn":
            userName = request.POST["userName"]
            password = request.POST["password"]
            user = authenticate(username=userName, password=password)
            if user is not None:
                request.session["userName"] = userName
                login(request, user)
                return redirect('/ors/welcome/')
            else:
                message = 'Invalid User'
        if request.POST.get('operation') == "signUp":
            return redirect("/ors/signup/")
    return render(request, "login.html", {'message': message})


def user_logout(request):
    logout(request)
    return redirect('/ors/signin/')

@login_required()
def add_marksheet(request):
    message = ''
    if request.method == "POST":
        marksheet = Marksheet()
        marksheet.rollNo = request.POST["rollNo"]
        marksheet.name = request.POST["name"]
        marksheet.physics = request.POST["physics"]
        marksheet.chemistry = request.POST["chemistry"]
        marksheet.maths = request.POST["maths"]

        if request.POST['operation'] == "save":
            message = 'Marksheet Added Successfully'
        if request.POST['operation'] == "update":
            marksheet.id = int(request.POST.get('id', 0))
            message = 'Marksheet Updated Successfully'
        if request.POST['operation'] == "list":
            return redirect("/ors/list/")

        marksheet.save()
    return render(request, "marksheet.html", {'message': message})

@login_required()
def marksheet_list(request):
    list = Marksheet.objects.all()
    return render(request, "marksheetlist.html", {"list": list})

@login_required()
def delete_marksheet(request, id):
    obj = Marksheet.objects.get(id=id)
    obj.delete()
    return redirect("/ors/list/")

@login_required()
def edit_marksheet(request, id):
    message = ''
    obj = Marksheet.objects.get(id=id)
    return render(request, "marksheet.html", {"form": obj, "id": id, 'message': message})
