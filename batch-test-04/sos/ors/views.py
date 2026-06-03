from django.shortcuts import render, redirect
from django.http import HttpResponse


def test_ors(request):
    return HttpResponse('<h1>test ors app</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    if request.method == 'POST':
        print(request.POST.get('firstName'))
        print(request.POST.get('lastName'))
        print(request.POST.get('loginId'))
        print(request.POST.get('password'))
        print(request.POST.get('dob'))
        print(request.POST.get('address'))
    return render(request, 'registration.html')


def user_signin(request):
    if request.method == 'POST':
        loginId = request.POST.get('loginId')
        password = request.POST.get('password')

        if loginId == 'admin' and password == 'admin':
            return redirect('/ors/welcome/')

    return render(request, 'login.html')
