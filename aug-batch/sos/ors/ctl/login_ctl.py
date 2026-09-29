from django.shortcuts import render, redirect


class LoginCtl:

    def __init__(self):
        self.form = {}

    def display(self, request):
        return render(request, 'login.html', {'form': self.form})

    def submit(self, request):
        return render(request, 'login.html', {'form': self.form})
