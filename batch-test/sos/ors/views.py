from django.shortcuts import render
from django.http import HttpResponse


def test_ors(request):
    return HttpResponse("<h1>Django Project ors</h1>")


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
