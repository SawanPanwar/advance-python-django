from django.db import connection

from ..models import User
from ..utility.data_validator import DataValidator
from django.core.paginator import Paginator


class UserService:

    def save(self, obj):
        is_new = obj.id == 0
        if is_new:
            obj.id = None
        obj.save()

    def delete(self, id):
        obj = self.get(id)
        obj.delete()

    def get(self, pk):
        try:
            obj = User.objects.get(id=pk)
            return obj
        except self.get_model().DoesNotExist:
            return None

    def find_by_login(self, login_id):
        try:
            obj = User.objects.get(login_id=login_id)
            return obj
        except self.get_model().DoesNotExist:
            return None

    def authenticate(self, login_id, password):
        query = User.objects.all()

        query = query.filter(login_id=login_id.strip())
        query = query.filter(password=password.strip())

        if len(query) > 0:
            return query[0]
        else:
            return None

    def search(self, params):

        page_no = int(params.get("page_no", 0))
        page_size = int(params.get('page_size', 0))

        query = User.objects.all()

        if (page_size == 0):
            return query

        # value = params.get("first_name", None)
        # if not DataValidator.is_null(value):
        #     query = query.filter(first_name__istartswith=value.strip())

        paginator = Paginator(query, page_size)

        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["start_index"] = (page_no - 1) * page_size

        return page_obj
