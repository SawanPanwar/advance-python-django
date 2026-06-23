from django.shortcuts import render


class WelcomeCtl:

    def display(self, request):
        return render(request, 'welcome.html')
