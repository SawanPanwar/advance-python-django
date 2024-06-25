from django.http import HttpResponse
from django.shortcuts import render, redirect

from .service.UserService import UserService


def test(request):
    print('helllo Django')
    return HttpResponse('<h1>Hello Django</h1>')


def register_user(request):
    message = ''
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
        message = 'User Registered Successfully'
    return render(request, 'UserRegistration.html', {'message': message})


def user_signin(request):
    message = ''
    if request.method == "POST":
        loginId = request.POST.get('loginId')
        password = request.POST.get('password')
        service = UserService()
        user_data = service.auth(loginId, password)
        if len(user_data) != 0:
            # request.session["firstName"] = user_data[0].get('firstName')
            return redirect("/ORS/welcome")
        else:
            message = 'login id & password is invalid'
    return render(request, "Login.html", {'message': message})


def welcome(request):
    return render(request, "Welcome.html")


def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}
    ]
    return render(request, "TestList.html", {"list": list})
