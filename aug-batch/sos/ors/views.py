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
    print(request.GET.get('firstName'))
    print(request.GET.get('lastName'))
    print(request.GET.get('loginId'))
    print(request.GET.get('password'))
    print(request.GET.get('dob'))
    print(request.GET.get('address'))
    return render(request, 'registration.html')


def user_signin(request):
    print(request.GET.get('loginId'))
    print(request.GET.get('password'))
    return render(request, 'login.html')
