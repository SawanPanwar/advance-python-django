from ..models import Booking
from ..utility.data_validator import DataValidator
from .base_service import BaseService


class BookingService(BaseService):

    def get_model(self):
        return Booking

    def get_unique(self):
        return []

    def populate(self, obj):
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
