from django.shortcuts import render, redirect
from django.http import HttpResponse


def test_ors(request):
    return HttpResponse("<h1>Django Project ors</h1>")


def welcome(request):
    return render(request, 'welcome.html')

def user_signup_test(request):
    print(request.GET.get('firstName'))
    print(request.GET.get('lastName'))
    print(request.GET.get('loginId'))
    print(request.GET.get('password'))
    print(request.GET.get('dob'))
    print(request.GET.get('address'))
    return render(request, 'registration.html')

def user_signup(request):
    print(request.POST.get('firstName'))
    print(request.POST.get('lastName'))
    print(request.POST.get('loginId'))
    print(request.POST.get('password'))
    print(request.POST.get('dob'))
    print(request.POST.get('address'))
    print(request.POST.get('csrfmiddlewaretoken'))
    return render(request, 'registration.html')

def user_signin(request):
    if request.method == "POST":
        if request.POST.get('operation') == "signIn":
            print(request.POST.get('loginId'))
            print(request.POST.get('password'))
        if request.POST.get('operation') == "signUp":
            return redirect("/ors/signup/")
    return render(request, 'login.html')
