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

    if request.method == "GET":
        return render(request, 'registration.html', {'form': form})

    if request.method == "POST":

        if request.POST.get('operation', '') == "signUp":
            form['first_name'] = request.POST.get('firstName')
            form['last_name'] = request.POST.get('lastName')
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')
            form['dob'] = request.POST.get('dob')
            form['address'] = request.POST.get('address')

            form['input_error'] = user_signup_validate(request)

            if form['input_error']['error']:
                return render(request, 'registration.html', {'form': form})

            try:
                UserService().add(form)
                form['message'] = 'User Registration Successfully...!!!'
                form['error'] = False
            except Exception as e:
                form['message'] = str(e)
                form['error'] = True
            return render(request, 'registration.html', {'form': form})

        if request.POST.get('operation', '') == "reset":
            return redirect('/ors/signup/')


def user_signin(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "GET":
        return render(request, 'login.html', {'form': form})

    if request.method == "POST":

        if request.POST.get('operation', '') == "signIn":
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')

            form['input_error'] = user_signin_validate(request)

            if form['input_error']['error']:
                return render(request, 'login.html', {'form': form})

            user_data = UserService().authenticate(form['login_id'], form['password'])

            if user_data:
                request.session['first_name'] = user_data[0].get('first_name')
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
    form = {}
    form['page_no'] = 1
    form['page_size'] = 5
    form['list'] = []

    if request.method == "GET":
        form['list'] = UserService().search(form)
        form['index'] = (form['page_no'] - 1) * form['page_size']
        form['has_previous'] = form['page_no'] == 1
        form['has_next'] = len(form['list']) < 5
        return render(request, "user_list.html", {"form": form})

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

        form['list'] = UserService().search(form)
        form['index'] = (form['page_no'] - 1) * form['page_size']
        form['has_previous'] = form['page_no'] == 1
        form['has_next'] = len(form['list']) < 5
        return render(request, "user_list.html", {"form": form})


def delete_user(request, id=0):
    UserService().delete(id)
    return redirect("/ors/list/")


def user_save(request, id=0):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "GET":

        if id > 0:
            user_data = UserService().get(id)
            form['id'] = user_data[0].get('id')
            form['first_name'] = user_data[0].get('first_name')
            form['last_name'] = user_data[0].get('last_name')
            form['login_id'] = user_data[0].get('login_id')
            form['password'] = user_data[0].get('password')
            form['dob'] = user_data[0].get('dob').strftime('%Y-%m-%d')
            form['address'] = user_data[0].get('address')

        return render(request, 'user.html', {'form': form})

    if request.method == "POST":

        if request.POST.get('operation', '') == "save":
            form['first_name'] = request.POST.get('firstName')
            form['last_name'] = request.POST.get('lastName')
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')
            form['dob'] = request.POST.get('dob')
            form['address'] = request.POST.get('address')

            form['input_error'] = user_signup_validate(request)

            if form['input_error']['error']:
                return render(request, 'user.html', {'form': form})

            try:
                UserService().add(form)
                form['message'] = 'User Added Successfully...!!!'
                form['error'] = False
            except Exception as e:
                form['message'] = str(e)
                form['error'] = True
            return render(request, 'user.html', {'form': form})

        if request.POST.get('operation', '') == "update":
            form['id'] = int(request.POST.get('id', 0))
            form['first_name'] = request.POST.get('firstName')
            form['last_name'] = request.POST.get('lastName')
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')
            form['dob'] = request.POST.get('dob')
            form['address'] = request.POST.get('address')

            form['input_error'] = user_signup_validate(request)

            if form['input_error']['error']:
                return render(request, 'user.html', {'form': form})

            try:
                UserService().update(form)
                form['message'] = 'User Updated Successfully...!!!'
                form['error'] = False
            except Exception as e:
                form['message'] = str(e)
                form['error'] = True
            return render(request, 'user.html', {'form': form})

        if request.POST.get('operation', '') == "reset":
            return redirect('/ors/save/')

        if request.POST.get('operation', '') == "list":
            return redirect('/ors/list/')
