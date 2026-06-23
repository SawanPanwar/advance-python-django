from django.shortcuts import render


class WelcomeCtl:

    def display(self, request, operation='', id=0):
        return render(request, 'welcome.html')
