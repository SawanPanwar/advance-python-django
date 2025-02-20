from django.http import HttpResponse
from django.shortcuts import render


def test_ors(request):
    return HttpResponse("<h1>ORS Test</h1>")


def welcome(request):
    return render(request, 'Welcome.html')


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