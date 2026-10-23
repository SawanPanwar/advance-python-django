from abc import abstractmethod

from ..models import Role
from ..utility.data_validator import DataValidator
from django.core.paginator import Paginator


class BaseDAO:

    def save(self, obj):
        duplicate = self.find_by_unique_key(obj)

        if obj.id > 0:
            duplicate = duplicate.exclude(id=obj.id)

        if duplicate.exists():
            raise Exception(self.get_lable(), 'already exist')

        if obj.id == 0:
            obj.id = None

        obj.save()

    def find_by_unique_key(self, obj):
        key = self.get_unique_key()
        value = getattr(obj, key)
        objs = self.get_model().objects.filter(key=value)
        return objs

    def get(self, pk):
        try:
            obj = self.get_model().objects.get(id=pk)
            return obj
        except self.get_model().DoesNotExist:
            return None

    def delete(self, id):
        obj = self.get(id)
        obj.delete()

    def search(self, params):

        page_no = int(params.get("page_no", 1))
        page_size = int(params.get('page_size', 0))

        query = self.get_model().objects.all()

        self.get_where_clause(query, params)

        if (page_size == 0):
            return query

        paginator = Paginator(query, page_size)

        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["index"] = (page_no - 1) * page_size

        return page_obj

    def get_where_clause(self, query, params):
        pass

    @abstractmethod
    def get_unique_key(self):
        pass

    @abstractmethod
    def get_lable(self):
        pass

    @abstractmethod
    def get_model(self):
        pass
