from django.http import HttpResponse
from abc import ABC, abstractmethod


class BaseCtl(ABC):
    preload_data = {}

    page_list = {}

    def __init__(self):
        self.form = {}
        self.form["id"] = 0
        self.form["message"] = ""
        self.form["error"] = False
        self.form["inputError"] = {}
        self.form["pageNo"] = 1

    def preload(self, request):
        pass

    def execute(self, request, params={}):
        self.preload(request)
        if "GET" == request.method:
            return self.display(request, params)
        elif "POST" == request.method:
            self.request_to_form(request.POST)
            if self.input_validation():
                return self.display(request, params)
            else:
                if (request.POST.get("operation") == "delete"):
                    return self.deleteRecord(request, params)
                elif (request.POST.get("operation") == "next"):
                    return self.next(request, params)
                elif (request.POST.get("operation") == "previous"):
                    return self.previous(request, params)
                else:
                    return self.submit(request, params)
        else:
            message = "Request is not supported"
            return HttpResponse(message)

    def deleteRecord(self, request, params={}):
        pass

    @abstractmethod
    def display(self, request, params={}):
        pass

    @abstractmethod
    def submit(self, request, params={}):
        pass

    def request_to_form(self, requestForm):
        pass

    def model_to_form(self, obj):
        pass

    def form_to_model(self, obj):
        pass

    def input_validation(self):
        self.form["error"] = False
        self.form["message"] = ""

    @abstractmethod
    def get_template(self):
        pass

    @abstractmethod
    def get_service(self):
        pass
