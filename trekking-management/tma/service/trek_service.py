from ..models import Trek
from ..utility.data_validator import DataValidator
from .base_service import BaseService


class TrekService(BaseService):

    def get_model(self):
        return Trek

    def get_unique(self):
        return ["trek_name"]

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):

        value = params.get("trek_name", "")
        if DataValidator.is_not_null(value):
            query = query.filter(Trek.trek_name.ilike(f"{value.strip()}%"))

        value = params.get("location", "")
        if DataValidator.is_not_null(value):
            query = query.filter(Trek.location.ilike(f"{value.strip()}%"))

        value = params.get("difficulty", "")
        if DataValidator.is_not_null(value):
            query = query.filter(Trek.difficulty == value)

        value = params.get("status", "")
        if DataValidator.is_not_null(value):
            query = query.filter(Trek.status == value)

        return query
