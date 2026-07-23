from abc import abstractmethod

from flask import render_template


class BaseCtl:

    def __init__(self):
        self.form = {
            'id': 0,
            'message': '',
            'error': False,
            'input_error': {},
            'page_no': 1,
            'page_size': 5
        }
        self.preload_data = {}
        self.page_list = []

    def preload(self, request):
        return self.preload_data

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

            if params['operation'] == 'delete' and params['id'] > 0:
                self.get_service().delete(params['id'])

            if params['operation'] == 'edit' and params['id'] > 0:
                obj = self.get_service().get(params['id'])

                if obj:
                    self.model_to_form(obj)

            return self.display(request, params)

        if request.method == "POST":

            self.request_to_form(request)

            if self.input_validation(request):
                return render_template(self.get_template(), form=self.form, preload_data=self.preload(request))

            return self.submit(request, params)
