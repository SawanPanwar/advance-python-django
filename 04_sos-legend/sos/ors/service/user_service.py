from django.db import connection

from ..models import User
from ..utility.data_validator import DataValidator
from django.core.paginator import Paginator


class UserService:

    def save(self, obj):
        print('user service orm save()')
        duplicate = self.find_by_login(obj.login_id)

        if obj.id > 0:
            duplicate = duplicate.exclude(id=obj.id)

        if duplicate.exists():
            raise Exception('Login ID already exist')

        if obj.id == 0:
            obj.id = None

        obj.save()

    def get(self, pk):
        print('user service orm get()')
        try:
            obj = User.objects.get(id=pk)
            return obj
        except User.DoesNotExist:
            return None

    def delete(self, id):
        print('user service orm delete()')
        obj = self.get(id)
        obj.delete()

    def find_by_login(self, login_id):
        print('user service orm find_by_login()')
        obj = User.objects.filter(login_id=login_id)
        return obj

    def authenticate(self, login_id, password):
        print('user service orm authenticate()')
        query = User.objects.all()

        query = query.filter(login_id=login_id.strip())
        query = query.filter(password=password.strip())

        if len(query) > 0:
            return query.first()
        else:
            return None

    def search(self, params):
        print('user service orm search()')

        page_no = int(params.get("page_no", 1))
        page_size = int(params.get('page_size', 0))

        query = User.objects.all()

        value = params.get("first_name", '')
        if DataValidator.is_not_null(value):
            query = query.filter(first_name__istartswith=value.strip())

        if (page_size == 0):
            return query

        paginator = Paginator(query, page_size)

        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["index"] = (page_no - 1) * page_size

        return page_obj
