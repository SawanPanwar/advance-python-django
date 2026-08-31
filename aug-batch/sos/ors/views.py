from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def test_ors(request):
    return HttpResponse('<h1>test ors app</h1>')


def display(request):
    return HttpResponse('<h1>this is ors display function</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    return render(request, 'registration.html')

def user_signin(request):
    return render(request, 'login.html')
