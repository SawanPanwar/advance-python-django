from django.http import HttpResponse
from django.shortcuts import render


def test_ors(request):
    return HttpResponse('<h1>This is  my ORS App</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    return render(request, 'registration.html')


def user_signin(request):
    return render(request, 'login.html')
