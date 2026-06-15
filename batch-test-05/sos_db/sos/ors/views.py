from django.shortcuts import render
from .service.user_service import UserService


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    message = ''

    if request.method == "POST":
        form = {}
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        user_service = UserService()
        try:
            user_service.add(form)
            message = 'User Registration Successfully...!!!'
        except Exception as e:
            message = e

    return render(request, 'registration.html', {'message': message})
