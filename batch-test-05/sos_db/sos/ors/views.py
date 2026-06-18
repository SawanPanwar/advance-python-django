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


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "POST":

        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        form['input_error'] = user_signup_validate(request)

        if not form['input_error']['error']:
            user_service = UserService()
            try:
                user_service.add(form)
                form['message'] = 'User Registration Successfully...!!!'
                form['error'] = False
            except Exception as e:
                form['message'] = e
                form['error'] = True

    return render(request, 'registration.html', {'form': form})


def user_signin(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "POST":

        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')

        form['input_error'] = user_signin_validate(request)

        if not form['input_error']['error']:
            user_service = UserService()
            user_data = user_service.authenticate(form['login_id'], form['password'])
            if len(user_data) > 0:
                request.session['first_name'] = user_data[0].get('firstName')
                return redirect('/ors/welcome/')
            else:
                form['message'] = 'Login ID & Password Invalid'
                form['error'] = True
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    request.session['first_name'] = None
    return redirect('/ors/signin/')


def user_list(request):
    form = {}
    form['page_no'] = 1
    form['page_size'] = 5
    form['list'] = []

    if request.method == "POST":
        if request.POST.get('operation', '') == "next":
            form['page_no'] = int(request.POST['pageNo'])
            form['page_no'] += 1
        if request.POST.get('operation', '') == "previous":
            form['page_no'] = int(request.POST['pageNo'])
            form['page_no'] -= 1
        if request.POST.get('operation', '') == "search":
            form['first_name'] = request.POST['firstName']

    user_service = UserService()
    user_list = user_service.search(form)
    form['list'] = user_list
    form['index'] = (form['page_no'] - 1) * form['page_size']

    return render(request, "userlist.html", {"form": form})


def delete_user(request, id=0):
    user_service = UserService()
    user_service.delete(id)
    return redirect('/ors/list/')


def user_save(request, id=0):
    form = {
        "id": 0
    }
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "GET" and id > 0:
        user_service = UserService()
        user_data = user_service.get(id)
        form['id'] = user_data[0].get('id')
        form['first_name'] = user_data[0].get('firstName')
        form['last_name'] = user_data[0].get('lastName')
        form['login_id'] = user_data[0].get('loginId')
        form['password'] = user_data[0].get('password')
        form['dob'] = user_data[0].get('dob')
        form['address'] = user_data[0].get('address')

    if request.method == "POST":
        form['id'] = int(request.POST.get('id', 0))
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        form['input_error'] = user_signup_validate(request)

        if not form['input_error']['error']:
            user_service = UserService()
            try:
                if form['id'] > 0:
                    user_service.update(form)
                    form['message'] = 'User Updated Successfully...!!!'
                    form['error'] = False
                else:
                    user_service.add(form)
                    form['message'] = 'User Added Successfully...!!!'
                    form['error'] = False
            except Exception as e:
                form['message'] = e
                form['error'] = True

    return render(request, 'user.html', {'form': form})
