from django.shortcuts import render, redirect

from .models import User
from .service.user_service import UserService
from .utility.data_validator import DataValidator


def init_form():
    form = {}
    form['id'] = 0
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}
    form['page_no'] = 1
    form['page_size'] = 5
    form['list'] = []
    return form


def request_to_form(request):
    form = {}
    form['id'] = int(request.POST.get('id', 0))
    form['first_name'] = request.POST.get('firstName')
    form['last_name'] = request.POST.get('lastName')
    form['login_id'] = request.POST.get('loginId')
    form['password'] = request.POST.get('password')
    form['dob'] = request.POST.get('dob')
    form['address'] = request.POST.get('address')
    return form


def form_to_model(form, obj):
    obj.id = form['id']
    obj.first_name = form['first_name']
    obj.last_name = form['last_name']
    obj.login_id = form['login_id']
    obj.password = form['password']
    obj.dob = form['dob']
    obj.address = form['address']
    return obj


def model_to_form(obj):
    form = {}
    form['id'] = obj.id
    form['first_name'] = obj.first_name
    form['last_name'] = obj.last_name
    form['login_id'] = obj.login_id
    form['password'] = obj.password
    form['dob'] = obj.dob.strftime('%Y-%m-%d')
    form['address'] = obj.address
    return form


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
    if request.method == "GET":
        form = init_form()
        return render(request, 'registration.html', {'form': form})

    if request.method == "POST":

        if request.POST.get('operation', '') == "signUp":

            form = init_form()

            form.update(request_to_form(request))

            form['input_error'] = user_signup_validate(request)

            if form['input_error']['error']:
                return render(request, 'registration.html', {'form': form})

            try:
                user = form_to_model(form, User())
                UserService().save(user)
                form['message'] = 'User Registration Successfully...!!!'
                form['error'] = False
            except Exception as e:
                form['message'] = str(e)
                form['error'] = True
            return render(request, 'registration.html', {'form': form})

        if request.POST.get('operation', '') == "reset":
            return redirect('/ors/signup/')


def user_signin(request):
    if request.method == "GET":
        form = init_form()
        return render(request, 'login.html', {'form': form})

    if request.method == "POST":
        form = init_form()

        if request.POST.get('operation', '') == "signIn":
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')

            form['input_error'] = user_signin_validate(request)

            if form['input_error']['error']:
                return render(request, 'login.html', {'form': form})

            user = UserService().authenticate(form['login_id'], form['password'])

            if user:
                request.session['first_name'] = user.first_name
                return redirect('/ors/welcome/')
            else:
                form['message'] = 'Login ID & Password Invalid'
                form['error'] = True

            return render(request, 'login.html', {'form': form})

        if request.POST.get('operation', '') == "signUp":
            return redirect('/ors/signup/')


def user_logout(request):
    request.session['first_name'] = None
    return redirect('/ors/signin/')


def user_list(request):
    if request.method == "GET":
        form = init_form()
        form['list'] = UserService().search(form)
        return render(request, "user_list.html", {"form": form})

    if request.method == "POST":
        form = init_form()

        if request.POST['operation'] == "next":
            form['page_no'] = int(request.POST.get('pageNo'))
            form['page_no'] += 1

        if request.POST['operation'] == "previous":
            form['page_no'] = int(request.POST.get('pageNo'))
            form['page_no'] -= 1

        if request.POST['operation'] == "search":
            form['page_no'] = 1
            form['first_name'] = request.POST.get('firstName')

        form['list'] = UserService().search(form)
        return render(request, "user_list.html", {"form": form})


def delete_user(request, id=0):
    UserService().delete(id)
    return redirect("/ors/list/")


def user_save(request, id=0):
    if request.method == "GET":
        form = init_form()

        if id > 0:
            user = UserService().get(id)

            form.update(model_to_form(user))

        return render(request, 'user.html', {'form': form})

    if request.method == "POST":

        operation = request.POST.get('operation', '')

        if operation in ['save', 'update']:

            form = init_form()

            form.update(request_to_form(request))

            form['input_error'] = user_signup_validate(request)

            if form['input_error']['error']:
                return render(request, 'user.html', {'form': form})

            try:
                user = form_to_model(form, User())
                UserService().save(user)
                if form['id'] > 0:
                    form['message'] = 'User Updated Successfully...!!!'
                    form['error'] = False
                else:
                    form['message'] = 'User Added Successfully...!!!'
                    form['error'] = False

            except Exception as e:
                form['message'] = str(e)
                form['error'] = True

            return render(request, 'user.html', {'form': form})

        if operation == "reset":
            return redirect('/ors/save/')

        if operation == "list":
            return redirect('/ors/list/')
