from .trek_service import TrekService
from .user_service import UserService
from ..models import StaffAssignment
from ..utility.data_validator import DataValidator
from .base_service import BaseService


class StaffAssignmentService(BaseService):

    def get_model(self):
        return StaffAssignment

    def get_unique(self):
        return []

    def populate(self, obj):
        staff = UserService().get(obj.staff_id)
        obj.staff_name = staff.first_name + ' ' + staff.last_name

        trek = TrekService().get(obj.trek_id)
        obj.trek_name = trek.trek_name

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
