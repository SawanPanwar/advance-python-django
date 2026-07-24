from .trek_service import TrekService
from .user_service import UserService
from ..models import Booking
from ..utility.data_validator import DataValidator
from .base_service import BaseService


class BookingService(BaseService):

    def get_model(self):
        return Booking

    def get_unique(self):
        return []

    def populate(self, obj):
        user = UserService().get(obj.user_id)
        obj.user_name = user.first_name + ' ' + user.last_name

        trek = TrekService().get(obj.trek_id)
        obj.trek_name = trek.trek_name

        return obj

    def get_where_conditions(self, query, params):

        value = params.get("user_id", "")
        if DataValidator.is_not_null(value):
            query = query.filter(Booking.user_id == value)

        value = params.get("trek_id", "")
        if DataValidator.is_not_null(value):
            query = query.filter(Booking.trek_id == value)

        value = params.get("booking_status", "")
        if DataValidator.is_not_null(value):
            query = query.filter(Booking.booking_status == value)

        return query
