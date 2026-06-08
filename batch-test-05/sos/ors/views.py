from django.shortcuts import render

from django.http import HttpResponse


def test_ors(request):
    return HttpResponse('<h1>welcome to ors app</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    return render(request, 'registration.html')


def user_signin(request):
    return render(request, 'login.html')
