from abc import ABC, abstractmethod
from .. import db


class DuplicateValueError(Exception):
    pass


class BaseService(ABC):

    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_unique(self):
        return []

    @abstractmethod
    def populate(self, obj):
        return obj

    @abstractmethod
    def get_where_conditions(self, query, params):
        return query

    def find_by_unique_key(self, obj):
        query = self.get_model().query

        for key in self.get_unique():
            query = query.filter(getattr(self.get_model(), key) == getattr(obj, key))

        return query

    def check_by_unique_key(self, obj):
        errors = []

        for key in self.get_unique():
            value = getattr(obj, key)

            query = self.get_model().query.filter(getattr(self.get_model(), key) == value)

            if obj.id:
                query = query.filter(self.get_model().id != obj.id)

            if query.first():
                errors.append(f"{key}='{value}' already exists")

        if errors:
            raise DuplicateValueError("; ".join(errors))

    def save(self, obj):
        self.check_by_unique_key(obj)

        obj = self.populate(obj)

        if obj.id:
            db.session.merge(obj)
        else:
            db.session.add(obj)

        db.session.commit()

        return obj

    def delete(self, pk):
        obj = self.get(pk)

        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get(self, pk):
        return self.get_model().query.get(pk)

    def search(self, params):
        page_no = int(params.get("page_no", 1))
        page_size = int(params.get("page_size", 0))

        query = self.get_model().query

        query = self.get_where_conditions(query, params)

        if page_size == 0:
            return query.all()

        pagination = query.paginate(
            page=page_no,
            per_page=page_size,
            error_out=False
        )

        params["has_next"] = pagination.has_next
        params["has_previous"] = pagination.has_prev
        params["index"] = (page_no - 1) * page_size

        return pagination.items
