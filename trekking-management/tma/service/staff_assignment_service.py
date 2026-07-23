from ..models import StaffAssignment
from ..utility.data_validator import DataValidator
from .base_service import BaseService


class StaffAssignmentService(BaseService):

    def get_model(self):
        return StaffAssignment

    def get_unique(self):
        return []

    def populate(self, obj):
        return obj

    def get_where_conditions(self, query, params):

        value = params.get("staff_id", "")
        if DataValidator.is_not_null(value):
            query = query.filter(StaffAssignment.staff_id == value)

        value = params.get("trek_id", "")
        if DataValidator.is_not_null(value):
            query = query.filter(StaffAssignment.trek_id == value)

        value = params.get("status", "")
        if DataValidator.is_not_null(value):
            query = query.filter(StaffAssignment.status == value)

        return query
