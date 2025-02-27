from django.http import HttpResponse
from django.shortcuts import render, redirect
from .service.UserService import UserService


def test_ors(request):
    return HttpResponse("<h1>ORS Test</h1>")


def test_user_signup(request):
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    loginId = request.POST.get('loginId')
    password = request.POST.get('password')
    dob = request.POST.get('dob')
    address = request.POST.get('address')
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken')

    print(firstName)
    print(lastName)
    print(loginId)
    print(password)
    print(dob)
    print(address)
    print(csrfmiddlewaretoken)
    return render(request, 'UserRegistration.html')


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
    return render(request, 'UserRegistration.html')


def user_signin(request):
    if request.method == "POST":
        loginId = request.POST.get('loginId')
        password = request.POST.get('password')
        service = UserService()
        user_data = service.auth(loginId, password)
        if len(user_data) != 0:
            request.session['firstName'] = user_data[0].get('firstName')
            return redirect('/ORS/welcome')
            # return render(request, 'Welcome.html', {'firstName': user_data[0].get('firstName')})
    return render(request, 'Login.html')


def welcome(request):
    return render(request, 'Welcome.html')

def logout(request):
    request.session['firstName'] = None
    return redirect('/ORS/signin')
