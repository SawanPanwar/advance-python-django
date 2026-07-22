from ors import db
from ors.models import User
from ors.utility.data_validator import DataValidator


class UserService:

    def save(self, obj):
        print("user service save()")

        duplicate = self.find_by_login(obj.login_id)

        if obj.id:
            duplicate = duplicate.filter(User.id != obj.id)

        if duplicate.first():
            raise Exception("Login ID already exists")

        if obj.id:
            db.session.merge(obj)
        else:
            db.session.add(obj)

        db.session.commit()

    def get(self, pk):
        print("user service get()")

        return User.query.get(pk)

    def delete(self, pk):
        print("user service delete()")

        obj = self.get(pk)

        if obj:
            db.session.delete(obj)
            db.session.commit()

    def find_by_login(self, login_id):
        print("user service find_by_login()")

        return User.query.filter_by(login_id=login_id)

    def authenticate(self, login_id, password):
        print("user service authenticate()")

        return User.query.filter_by(
            login_id=login_id.strip(),
            password=password.strip()
        ).first()

    def search(self, params):
        print("user service search()")

        page_no = int(params.get("page_no", 1))
        page_size = int(params.get("page_size", 0))

        query = User.query

        value = params.get("first_name", "")

        if DataValidator.is_not_null(value):
            query = query.filter(
                User.first_name.ilike(f"{value.strip()}%")
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