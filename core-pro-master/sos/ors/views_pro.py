from django.shortcuts import render, redirect
from .service.user_service import UserService
from .utility.data_validator import DataValidator

def init_form():
    form = {}
    form['id'] = 0
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}
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


def dict_to_form(user_data):
    form = {}
    form['id'] = user_data.get('id')
    form['first_name'] = user_data.get('first_name')
    form['last_name'] = user_data.get('last_name')
    form['login_id'] = user_data.get('login_id')
    form['password'] = user_data.get('password')
    form['dob'] = user_data.get('dob').strftime('%Y-%m-%d')
    form['address'] = user_data.get('address')
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
    form = init_form()

    if request.method == "GET":
        return render(request, 'registration.html', {'form': form})

    if request.method == "POST":
        form.update(request_to_form(request))
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


def user_signin(request):
    form = init_form()

    if request.method == "GET":
        return render(request, 'login.html', {'form': form})

    if request.method == "POST":
        operation = request.POST.get('operation', '')

        if operation == "signIn":
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')

            form['input_error'] = user_signin_validate(request)

            if form['input_error']['error']:
                return render(request, 'login.html', {'form': form})

            user_data = UserService().authenticate(form['login_id'], form['password'])

            if user_data:
                request.session['first_name'] = user_data[0].get('first_name')
                uri = request.POST.get('uri')
                if uri != '':
                    return redirect(uri)
                else:
                    return redirect('/ors/welcome/')
            else:
                form['message'] = 'Login ID & Password Invalid'
                form['error'] = True

        if operation == "signUp":
            return redirect('/ors/signup/')

        return render(request, 'login.html', {'form': form})


def user_logout(request):
    request.session['first_name'] = None
    request.session.flush()
    return redirect('/ors/signin/')


def user_list(request):
    form = {}
    form['page_no'] = 1
    form['page_size'] = 5
    form['list'] = []

    if request.method == "GET":
        user_service = UserService()
        user_list = user_service.search(form)
        form['list'] = user_list
        form['index'] = (form['page_no'] - 1) * form['page_size']
        form['has_previous'] = form['page_no'] == 1
        form['has_next'] = len(user_list) < 5
        return render(request, "userlist.html", {"form": form})

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
        form['has_previous'] = form['page_no'] == 1
        form['has_next'] = len(user_list) < 5

        return render(request, "userlist.html", {"form": form})


def delete_user(request, id=0):
    UserService().delete(id)
    return redirect('/ors/list/')


def user_save(request, id=0):
    form = init_form()

    if request.method == "GET":
        if id > 0:
            user_service = UserService()
            user_data = user_service.get(id)
            form.update(dict_to_form(user_data[0]))
        return render(request, 'user.html', {'form': form})

    if request.method == "POST":
        operation = request.POST.get('operation', '')
        user_service = UserService()

        if operation == 'save':
            form.update(request_to_form(request))
            form['input_error'] = user_signup_validate(request)

            if form['input_error']['error']:
                return render(request, 'user.html', {'form': form})

            try:
                user_service.add(form)
                form['message'] = 'User Added Successfully...!!!'
            except Exception as e:
                form['message'] = str(e)
                form['error'] = True

        elif operation == 'update':
            form.update(request_to_form(request))
            form['input_error'] = user_signup_validate(request)

            if form['input_error']['error']:
                return render(request, 'user.html', {'form': form})

            try:
                user_service.update(form)
                form['message'] = 'User Updated Successfully...!!!'
            except Exception as e:
                form['message'] = str(e)
                form['error'] = True

        elif operation == "reset":
            return redirect('/ors/save/')

        elif operation == "list":
            return redirect('/ors/list/')

        return render(request, 'user.html', {'form': form})
