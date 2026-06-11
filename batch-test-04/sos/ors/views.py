from django.shortcuts import render, redirect
from django.http import HttpResponse
from .service.UserService import UserService


def test_ors(request):
    return HttpResponse('<h1>test ors app</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    message = ''
    if request.method == 'POST':
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()

        user_exist = service.findByLogin(params['loginId'])

        if len(user_exist) > 0:
            message = 'Login Already Exist..!!'
        else:
            service.add(params)
            message = 'User Registered Successfully..!!'

    return render(request, 'registration.html', {'message': message})


def user_signin(request):
    message = ''

    if request.method == 'POST':
        operation = request.POST.get('operation')
        if operation == 'signIn':
            loginId = request.POST.get('loginId')
            password = request.POST.get('password')
            uri = request.POST.get('uri')
            service = UserService()
            user_data = service.auth(loginId, password)

            if len(user_data) > 0:
                request.session['firstName'] = user_data[0].get('firstName')
                if uri != '':
                    return redirect(uri)
                else:
                    return redirect('/ors/welcome/')
                # return render(request, 'welcome.html', {'name': user_data[0].get('firstName')})
            else:
                message = 'Login & Password Invalid..!!'

        if operation == 'signUp':
            return redirect('/ors/signup/')

    return render(request, 'login.html', {'message': message})


def user_logout(request):
    request.session['firstName'] = None
    return redirect('/ors/signin/')


def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}
    ]
    return render(request, "testlist.html", {"list": list})


def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5

    if request.method == "POST":
        if request.POST['operation'] == "next":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] += 1
        if request.POST['operation'] == "previous":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] -= 1
        if request.POST['operation'] == "search":
            params['firstName'] = request.POST['firstName']

    service = UserService()
    list = service.search(params)
    index = (params['pageNo'] - 1) * 5
    return render(request, "userlist.html", {"list": list, 'index': index, 'pageNo': params['pageNo']})


def user_save(request, id=0):
    form = {
        'message': '',
        'error': False
    }
    service = UserService()

    if request.method == 'GET' and id > 0:
        user_data = service.get(id)
        user_data[0]['dob'] = user_data[0]['dob'].strftime('%Y-%m-%d')
        form = user_data[0]

    if request.method == 'POST':
        form['firstName'] = request.POST.get('firstName')
        form['lastName'] = request.POST.get('lastName')
        form['loginId'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        user_exist = service.findByLogin(form['loginId'])

        if request.POST['operation'] == "save":
            if len(user_exist) > 0:
                form['message'] = 'Login Already Exist..!!'
                form['error'] = True
            else:
                service.add(form)
                form['message'] = 'User Added Successfully..!!'
                form['error'] = False
        if request.POST['operation'] == "update":
            form['id'] = id
            if len(user_exist) > 0 and user_exist[0]['id'] != id:
                form['message'] = 'Login Already Exist..!!'
                form['error'] = True
            else:
                service.update(form)
                form['message'] = 'User Updated Successfully..!!'
                form['error'] = False
    return render(request, 'user.html', {'form': form})


def delete_user(request, id=0):
    service = UserService()
    service.delete(id)
    return redirect("/ors/list/")
