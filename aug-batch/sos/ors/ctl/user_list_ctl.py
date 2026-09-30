from django.shortcuts import render

from ..service.user_service import UserService


class UserListCtl:

    def __init__(self):
        self.form = {}
        self.form['message'] = ''
        self.form['error'] = False
        self.form['page_no'] = 1
        self.form['page_size'] = 5
        self.form['list'] = []

    def request_to_form(self, request):
        self.form['first_name'] = request.POST.get('firstName')

    def display(self, request):
        self.form['list'] = UserService().search(self.form)
        return render(request, "user_list.html", {"form": self.form})

    def submit(self, request):

        if request.POST['operation'] == "next":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] += 1

        if request.POST['operation'] == "previous":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] -= 1

        if request.POST['operation'] == "search":
            self.form['page_no'] = 1
            self.request_to_form(request)

        self.form['list'] = UserService().search(self.form)
        return render(request, "user_list.html", {"form": self.form})
