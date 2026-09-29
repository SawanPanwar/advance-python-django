from django.shortcuts import render


class RegistrationCtl:

    def __init__(self):
        self.form = {}

    def display(self, request):
        return render(request, 'registration.html', {'form': self.form})

    def submit(self, request):
        return render(request, 'registration.html', {'form': self.form})
