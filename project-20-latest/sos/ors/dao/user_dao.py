from .base_dao import BaseDAO
from ..models import User
from ..utility.data_validator import DataValidator


class UserDAO(BaseDAO):

    def get_unique_key(self):
        return "login_id"

    def get_model(self):
        return User

    def get_label(self):
        return "Login ID"

    def get_where_clause(self, query, params):
        value = params.get("first_name", "")

        if DataValidator.is_not_null(value):
            query = query.filter(first_name__istartswith=value.strip)

        return query
