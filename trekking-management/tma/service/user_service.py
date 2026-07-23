from ..models import User
from ..utility.data_validator import DataValidator
from .base_service import BaseService


class UserService(BaseService):

    def get_model(self):
        return User

    def get_unique(self):
        return ["email"]

    def populate(self, obj):
        return obj

    def authenticate(self, email, password):
        return User.query.filter_by(
            email=email.strip(),
            password=password.strip()
        ).first()

    def get_where_conditions(self, query, params):

        value = params.get("first_name", "")
        if DataValidator.is_not_null(value):
            query = query.filter(User.first_name.ilike(f"{value.strip()}%"))

        value = params.get("last_name", "")
        if DataValidator.is_not_null(value):
            query = query.filter(User.last_name.ilike(f"{value.strip()}%"))

        value = params.get("email", "")
        if DataValidator.is_not_null(value):
            query = query.filter(User.email.ilike(f"{value.strip()}%"))

        value = params.get("role", "")
        if DataValidator.is_not_null(value):
            query = query.filter(User.role == value)

        value = params.get("status", "")
        if DataValidator.is_not_null(value):
            query = query.filter(User.status == value)

        return query
