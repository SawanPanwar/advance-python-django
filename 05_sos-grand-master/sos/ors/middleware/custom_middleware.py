from django.http import HttpResponse
from django.shortcuts import render, redirect


class SimpleMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        SimpleMiddleware.count += 1
        print("Middleware = ", SimpleMiddleware.count)
        # print('======>>>>>>>>>>>', self.get_response)
        res = self.get_response(request)
        # return HttpResponse("<center><h1>Welcome to Middleware</h1></center>")
        return res


class FrontCtlMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.form = {}

    def __call__(self, request):

        if request.path_info in ['/', '/ors/signin/', '/ors/signup/', '/ors/welcome/', '/ors/logout/']:
            return self.get_response(request)

        uri = request.path_info

        if request.session.get('first_name', None) == None:
            self.form['message'] = 'Session expired... plz login again..!!'
            self.form['error'] = True
            return render(request, 'login.html', {'form': self.form, 'uri': uri})

        return self.get_response(request)
