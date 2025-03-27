from django.shortcuts import render


class FrontCtlMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.form = {}

    def __call__(self, request):

        if request.path_info in ['/', '/ORS/Login/', '/ORS/Registration/', '/ORS/Welcome/', '/ORS/Logout/',
                                 '/ORS/ForgetPassword/']:
            return self.get_response(request)

        if request.session.get('user') == None:
            self.form['message'] = 'Session expired... plz login again..!!'
            return render(request, "Login.html", {'form': self.form})
        else:
            return self.get_response(request)
