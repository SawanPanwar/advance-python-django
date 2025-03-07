from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


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
