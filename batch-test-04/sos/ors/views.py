from django.shortcuts import render, redirect
from django.http import HttpResponse
from .service.UserService import UserService


def test_ors(request):
    return HttpResponse('<h1>test ors app</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    message = ''
    if request.method == 'POST':
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()

        user_exist = service.findByLogin(params['loginId'])

        if len(user_exist) > 0:
            message = 'Login Already Exist..!!'
        else:
            service.add(params)
            message = 'User Registered Successfully..!!'

    return render(request, 'registration.html', {'message': message})


def user_signin(request):
    message = ''

    if request.method == 'POST':
        operation = request.POST.get('operation')
        if operation == 'signIn':
            loginId = request.POST.get('loginId')
            password = request.POST.get('password')
            service = UserService()
            user_data = service.auth(loginId, password)

            if len(user_data) > 0:
                request.session['firstName'] = user_data[0].get('firstName')
                return redirect('/ors/welcome/')
                # return render(request, 'welcome.html', {'name': user_data[0].get('firstName')})
            else:
                message = 'Login & Password Invalid..!!'

        if operation == 'signUp':
            return redirect('/ors/signup/')

    return render(request, 'login.html', {'message': message})


def user_logout(request):
    request.session['firstName'] = None
    return redirect('/ors/signin/')


def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}
    ]
    return render(request, "testlist.html", {"list": list})


def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5

    service = UserService()
    list = service.search(params)
    index = (params['pageNo'] - 1) * 5
    return render(request, "userlist.html", {"list": list, 'index': index})
