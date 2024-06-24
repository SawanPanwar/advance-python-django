from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    print('helllo Django')
    return HttpResponse('<h1>Hello Django</h1>')


def register_user(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        loginId = request.POST.get('loginId')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        print(firstName)
        print(lastName)
        print(loginId)
        print(password)
        print(dob)
        print(address)
    return render(request, 'UserRegistration.html')
