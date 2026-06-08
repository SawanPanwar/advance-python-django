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
                return redirect('/ors/welcome/')
            else:
                message = 'Login & Password Invalid..!!'

        if operation == 'signUp':
            return redirect('/ors/signup/')

    return render(request, 'login.html', {'message': message})
