from abc import ABC, abstractmethod
from flask import request, render_template


class BaseCtl(ABC):

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

    def preload(self):
        return self.preload_data

    def input_validation(self):
        pass

    def request_to_form(self, request):
        pass

    def form_to_model(self, obj):
        pass

    def model_to_form(self, obj):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def submit(self):
        pass

    @abstractmethod
    def get_service(self):
        pass

    @abstractmethod
    def get_template(self):
        pass

    def execute(self, operation="", id=0):
        if request.method == "GET":
            if operation == "delete" and id > 0:
                self.get_service().delete(id)
            if operation == "edit" and id > 0:
                obj = self.get_service().get(id)
                self.model_to_form(obj)
            return self.display()

        if request.method == "POST":
            self.request_to_form()
            if self.input_validation():
                return render_template(self.get_template(), form=self.form, preload_data=self.preload())
            return self.submit()
