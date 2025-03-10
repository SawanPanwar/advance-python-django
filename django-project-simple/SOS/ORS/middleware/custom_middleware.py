from django.http import HttpResponse
from django.shortcuts import render, redirect


class SimpleMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        SimpleMiddleware.count += 1
        print("Middleware = ", SimpleMiddleware.count)
        res = self.get_response(request)
        # return HttpResponse("<center><h1>Welcome to Middleware</h1></center>")
        return res


class FrontCtlMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path_info in ['/', '/ORS/signin/', '/ORS/signup/', '/ORS/welcome/', '/ORS/logout/']:
            return self.get_response(request)

        if request.session['firstName'] == None:
            message = 'Session expired... plz login again..!!'
            # return redirect('/ORS/signin/')
            return render(request, 'Login.html', {'message': message})

        return self.get_response(request)
