from django.http import HttpResponse
from django.shortcuts import render

from .service.user_service import UserService


# Create your views here.

def test_ors(request):
    return HttpResponse('<h1>test ors app</h1>')


def display(request):
    return HttpResponse('<h1>this is ors display function</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    if request.method == "POST":
        form = {}
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        service = UserService()
        service.add(form)

    return render(request, 'registration.html')


def user_signin(request):
    print(request.POST.get('loginId'))
    print(request.POST.get('password'))
    return render(request, 'login.html')
