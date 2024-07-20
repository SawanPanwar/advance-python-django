from django.shortcuts import render, redirect
from abc import ABC, abstractmethod


class BaseCtl(ABC):
    preload_data = {}
    page_list = {}

    @abstractmethod
    def display(self, request):
        pass

    @abstractmethod
    def submit(self, request):
        pass

    def preload(self, request):
        print("This is preload")

    def execute(self, request, operation="", id=0):
        self.preload(request)
        if "GET" == request.method:
            if operation == "Edit":
                return self.edit(request, id)
            return self.display(request)
        elif "POST" == request.method:
            if request.POST["operation"] == "delete":
                return self.delete(request)
            elif request.POST["operation"] == "next":
                return self.next(request)
            elif request.POST["operation"] == "previous":
                return self.previous(request)
            elif request.POST["operation"] == "add":
                return self.add(request)
            elif request.POST["operation"] == "SignUp":
                return self.signUp(request)
            else:
                return self.submit(request)

    @abstractmethod
    def get_service(self):
        pass

    @abstractmethod
    def get_template(self):
        pass
