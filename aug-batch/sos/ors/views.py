from django.http import HttpResponse
from django.shortcuts import render, redirect

from .service.user_service import UserService


def test_ors(request):
    return HttpResponse('<h1>test ors app</h1>')


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
    message = ''
    if request.method == "POST":
        form = {}
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')

        service = UserService()
        user_data = service.authenticate(form['login_id'], form['password'])

        if len(user_data) > 0:
            request.session['first_name'] = user_data[0].get('first_name')
            return render(request, 'welcome.html', {'name': user_data[0].get('first_name')})
        else:
            message = 'login & password invalid'

    return render(request, 'login.html', {'message': message})


def user_logout(request):
    request.session['first_name'] = None
    return redirect('/ors/signin/')
