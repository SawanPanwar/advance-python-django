from django.http import HttpResponse
from abc import ABC, abstractmethod


class BaseCtl(ABC):
    dynamic_preload = {}
    static_preload = {}
    page_list = {}

    def __init__(self):
        self.form = {}
        self.form["id"] = 0
        self.form["message"] = ""
        self.form["error"] = False
        self.form["inputError"] = {}
        self.form["pageNo"] = 1
        self.form["preload"] = {}

    def preload(self, request, id):
        pass

    def execute(self, request, params={}):
        self.preload(request, params)
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
                elif (request.POST.get("operation") == "new"):
                    return self.new(request, params)
                else:
                    return self.submit(request, params)
        else:
            message = "Request is not supported"
            return HttpResponse(message)

    @abstractmethod
    def display(self, request, params={}):
        pass

    @abstractmethod
    def submit(self, request, params={}):
        pass

    def request_to_form(self, requestForm):
        pass

    def form_to_model(self, obj):
        pass

    def model_to_form(self, obj):
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
