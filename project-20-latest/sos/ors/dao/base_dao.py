from abc import ABC, abstractmethod

from django.core.paginator import Paginator


class BaseDAO(ABC):

    def save(self, obj):
        duplicate = self.check_duplicate(obj)

        if obj.pk:
            duplicate = duplicate.exclude(pk=obj.pk)

        if duplicate.exists():
            raise Exception(f'{self.get_label()} already exist')

        if not obj.pk:
            obj.pk = None

        obj.save()

    def get(self, pk):
        try:
            return self.get_model().objects.get(pk=pk)
        except self.get_model().DoesNotExist:
            return None

    def delete(self, pk):
        obj = self.get(pk)
        obj.delete()

    def search(self, params):
        page_no = int(params.get("page_no", 1))
        page_size = int(params.get("page_size", 0))

        query = self.get_model().objects.all()
        query = self.get_where_clause(query, params)

        if page_size <= 0:
            return query

        paginator = Paginator(query, page_size)
        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["index"] = (page_obj.number - 1) * page_size

        return page_obj

    def check_duplicate(self, obj):
        key = self.get_unique_key()
        value = getattr(obj, key)

        objs = self.get_model().objects.filter(**{key: value})
        return objs

    def find_by_unique_key(self, key, value):
        objs = self.get_model().objects.filter(**{key: value})
        return objs

    def get_where_clause(self, query, params):
        return query

    @abstractmethod
    def get_unique_key(self):
        pass

    @abstractmethod
    def get_label(self):
        pass

    @abstractmethod
    def get_model(self):
        pass
