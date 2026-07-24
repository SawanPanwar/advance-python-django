from ..models import User, Trek, Booking, StaffAssignment
from ..utility.data_validator import DataValidator


class DashboardService:

    def get_admin_dashboard(self):
        data = {}

        data["total_trek"] = Trek.query.count()

        data["total_user"] = User.query.filter_by(role="User").count()

        data["total_staff"] = User.query.filter_by(role="Staff").count()

        data["total_booking"] = Booking.query.count()

        data["pending_staff"] = User.query.filter_by(role="Staff", status="Pending").count()

        return data

    def get_staff_dashboard(self, staff_id):
        data = {}

        data["assigned_trek"] = StaffAssignment.query.filter_by(staff_id=staff_id).count()

        data["booking_count"] = Booking.query.join(
            StaffAssignment,
            Booking.trek_id == StaffAssignment.trek_id
        ).filter(
            StaffAssignment.staff_id == staff_id
        ).count()

        return data

    def get_user_dashboard(self, user_id):
        data = {}

        data["available_trek"] = Trek.query.filter_by(status="Open").count()

        data["my_booking"] = Booking.query.filter_by(user_id=user_id).count()

        data["completed_trek"] = Booking.query.filter_by(
            user_id=user_id,
            booking_status="Completed"
        ).count()

        return data
