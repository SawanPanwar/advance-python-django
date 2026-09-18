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
            return redirect('/ors/welcome/')
        else:
            message = 'login & password invalid'

    return render(request, 'login.html', {'message': message})


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
