from abc import ABC, abstractmethod

from django.shortcuts import render


class BaseCtl:

    def __init__(self):
        self.form = {}
        self.form['id'] = 0
        self.form['message'] = ''
        self.form['error'] = False
        self.form['input_error'] = {}
        self.form['page_no'] = 1
        self.form['page_size'] = 5
        self.form['list'] = []

    def input_validation(self, request):
        pass

    def request_to_form(self, request):
        pass

    def form_to_model(self, obj):
        pass

    def model_to_form(self, obj):
        pass

    @abstractmethod
    def display(self, request, params={}):
        pass

    @abstractmethod
    def submit(self, request, params={}):
        pass

    @abstractmethod
    def get_service(self):
        pass

    @abstractmethod
    def get_template(self):
        pass

    def execute(self, request, params={}):

        if request.method == "GET":
            return self.display(request, params)

        if request.method == "POST":

            self.request_to_form(request)

            if self.input_validation(request):
                return render(request, self.get_template(), {'form': self.form})

            return self.submit(request, params)
