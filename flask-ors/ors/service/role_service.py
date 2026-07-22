from .. import db
from ..models import Role
from ..utility.data_validator import DataValidator


class RoleService:

    def save(self, obj):
        print("role service orm save()")

        duplicate = self.find_by_name(obj.name)

        if obj.id:
            duplicate = duplicate.filter(Role.id != obj.id)

        if duplicate.first():
            raise Exception("Name already exist")

        if obj.id:
            db.session.merge(obj)
        else:
            db.session.add(obj)

        db.session.commit()

    def get(self, pk):
        print("role service orm get()")

        return Role.query.get(pk)

    def delete(self, pk):
        print("role service orm delete()")

        obj = self.get(pk)

        if obj:
            db.session.delete(obj)
            db.session.commit()

    def find_by_name(self, name):
        print("role service orm find_by_name()")

        return Role.query.filter_by(name=name)

    def search(self, params):
        print("role service orm search()")

        page_no = int(params.get("page_no", 1))
        page_size = int(params.get("page_size", 0))

        query = Role.query

        value = params.get("name", "")

        if DataValidator.is_not_null(value):
            query = query.filter(
                Role.name.ilike(f"{value.strip()}%")
            )

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
