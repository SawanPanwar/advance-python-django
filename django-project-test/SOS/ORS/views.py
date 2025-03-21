from django.shortcuts import render

from django.http import HttpResponse


def test_ors(request):
    return HttpResponse('<h1>Welcome to ORS App</h1>')


def test_user_signup(request):
    if request.method == 'POST':
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


def welcome(request):
    return render(request, 'Welcome.html')


def user_signup(request):
    return render(request, 'UserRegistration.html')


def user_signin(request):
    return render(request, 'Login.html')
