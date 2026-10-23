from .base_dao import BaseDAO
from ..models import Role
from ..utility.data_validator import DataValidator
from django.core.paginator import Paginator


class RoleDAO(BaseDAO):

    def get_unique_key(self):
        return 'name'

    def get_model(self):
        return Role

    def get_lable(self):
        return 'Role Name'

    def get_where_clause(self, query, params):
        value = params.get("name", '')
        if DataValidator.is_not_null(value):
            query = query.filter(name__istartswith=value.strip())
