from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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

