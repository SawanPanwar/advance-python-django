from django.shortcuts import render, redirect
from django.http import HttpResponse
from .service.user_service import UserService


def test_ors(request):
    return HttpResponse("<h1>Django Project ors</h1>")


def welcome(request):
    return render(request, 'welcome.html')


def user_signup_test(request):
    print(request.GET.get('firstName'))
    print(request.GET.get('lastName'))
    print(request.GET.get('loginId'))
    print(request.GET.get('password'))
    print(request.GET.get('dob'))
    print(request.GET.get('address'))
    return render(request, 'registration.html')


def user_signup(request):
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
    return render(request, 'registration.html')


def user_signin(request):
    message = ''
    if request.method == "POST":
        if request.POST.get('operation') == "signIn":
            loginId = request.POST.get('loginId')
            password = request.POST.get('password')
            service = UserService()
            user_data = service.auth(loginId, password)
            if len(user_data) != 0:
                # return redirect('/ors/welcome')
                return render(request, 'welcome.html', {'firstName': user_data[0].get('firstName')})
            else:
                message = 'Login ID & Password Invalid'
        if request.POST.get('operation') == "signUp":
            return redirect("/ors/signup/")
    return render(request, 'login.html', {'message': message})
