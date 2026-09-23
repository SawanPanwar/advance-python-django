from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .service.user_service import UserService
from .utility.data_validator import DataValidator


def user_signup_validate(request):
    input_error = {}
    input_error['error'] = False
    if (DataValidator.is_null(request.POST.get("firstName", ''))):
        input_error['first_name'] = 'First Name is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("lastName", ''))):
        input_error['last_name'] = 'Last Name is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("loginId", ''))):
        input_error['login_id'] = 'Login ID is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("password", ''))):
        input_error['password'] = 'Password is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("dob", ''))):
        input_error['dob'] = 'DOB is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("address", ''))):
        input_error['address'] = 'Address is required'
        input_error['error'] = True
    return input_error


def user_signin_validate(request):
    input_error = {}
    input_error['error'] = False
    if (DataValidator.is_null(request.POST.get("loginId", ''))):
        input_error['login_id'] = 'Login ID is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("password", ''))):
        input_error['password'] = 'Password is required'
        input_error['error'] = True
    return input_error


def test_ors(request):
    return HttpResponse('<h1>test ors app</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "POST":

        if request.POST.get('operation', '') == "signUp":
            form['first_name'] = request.POST.get('firstName')
            form['last_name'] = request.POST.get('lastName')
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')
            form['dob'] = request.POST.get('dob')
            form['address'] = request.POST.get('address')

            form['input_error'] = user_signup_validate(request)

            if not form['input_error']['error']:
                try:
                    UserService().add(form)
                    form['message'] = 'User Registration Successfully...!!!'
                    form['error'] = False
                except Exception as e:
                    form['message'] = str(e)
                    form['error'] = True

        if request.POST.get('operation', '') == "reset":
            return redirect('/ors/signup/')

    return render(request, 'registration.html', {'form': form})


def user_signin(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "POST":

        if request.POST.get('operation', '') == "signIn":
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')

            form['input_error'] = user_signin_validate(request)

            if not form['input_error']['error']:

                user_data = UserService().authenticate(form['login_id'], form['password'])

                if user_data:
                    request.session['first_name'] = user_data[0].get('first_name')
                    return redirect('/ors/welcome/')
                else:
                    form['message'] = 'Login ID & Password Invalid'
                    form['error'] = True

        if request.POST.get('operation', '') == "signUp":
            return redirect('/ors/signup/')

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    request.session['first_name'] = None
    return redirect('/ors/signin/')


def test_list(request):
    list = [
        {"id": 1, "first_name": "Rahul", "last_name": "Sharma", "email": "rahul@gmail.com", "password": "rahul123"},
        {"id": 2, "first_name": "Priya", "last_name": "Verma", "email": "priya@gmail.com", "password": "priya123"},
        {"id": 3, "first_name": "Amit", "last_name": "Patel", "email": "amit@gmail.com", "password": "amit123"},
        {"id": 4, "first_name": "Neha", "last_name": "Singh", "email": "neha@gmail.com", "password": "neha123"},
        {"id": 5, "first_name": "Rohit", "last_name": "Gupta", "email": "rohit@gmail.com", "password": "rohit123"}
    ]
    return render(request, "test_list.html", {"list": list})


def user_list(request):
    form = {}
    form['page_no'] = 1
    form['page_size'] = 5

    if request.method == "POST":
        if request.POST['operation'] == "next":
            form['page_no'] = int(request.POST.get('pageNo'))
            form['page_no'] += 1

        if request.POST['operation'] == "previous":
            form['page_no'] = int(request.POST.get('pageNo'))
            form['page_no'] -= 1

        if request.POST['operation'] == "search":
            form['page_no'] = 1
            form['first_name'] = request.POST.get('firstName')

    service = UserService()
    list = service.search(form)
    index = (form['page_no'] - 1) * form['page_size']
    return render(request, "user_list.html", {"list": list, 'page_no': form['page_no'], 'index': index})


def delete_user(request, id=0):
    service = UserService()
    service.delete(id)
    return redirect("/ors/list/")


def user_save(request):
    if request.method == "POST":
        form = {}
        form['id'] = request.POST.get('id', 0)
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        service = UserService()

        if form['id'] != '' and int(form['id']) > 0:
            service.update(form)
        else:
            service.add(form)

    return render(request, 'user.html')


def edit_user(request, id=0):
    service = UserService()
    user_data = service.get(id)
    return render(request, 'user.html', {'data': user_data[0]})


def create_session(request):
    request.session['name'] = 'Admin'
    response = "<h1>Welcome To Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)


def access_session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)


def destroy_session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")


def set_cookies(request):
    key = "name"
    value = "abc"
    res = HttpResponse("<h1>cookie created..!!</h1>")
    res.set_cookie(key, value, max_age=20)
    return res


def get_cookies(request):
    value = request.COOKIES.get('name')
    html = "<h3><center> value = {} </center></h3>".format(value)
    return HttpResponse(html)
