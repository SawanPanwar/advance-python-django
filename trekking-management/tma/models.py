from . import db


class DropdownItem:

    def get_key(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class User(BaseModel, DropdownItem):
    __tablename__ = "tm_user"

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    mobile = db.Column(db.String(15))
    gender = db.Column(db.String(20))
    address = db.Column(db.String(255))

    role = db.Column(db.String(20), nullable=False)
    # Admin / Staff / User

    status = db.Column(db.String(20), default="Pending")

    # Pending / Approved / Active / Blacklisted

    def get_key(self):
        return self.id

    def get_value(self):
        return f"{self.first_name} {self.last_name}"


class Trek(BaseModel, DropdownItem):
    __tablename__ = "tm_trek"

    trek_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    difficulty = db.Column(db.String(20), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    total_slots = db.Column(db.Integer, nullable=False)
    available_slots = db.Column(db.Integer, nullable=False)

    price = db.Column(db.Float, default=0)

    description = db.Column(db.String(500))

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    status = db.Column(db.String(20), default="Pending")

    created_by = db.Column(db.Integer)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.trek_name


class StaffAssignment(BaseModel):
    __tablename__ = "tm_staff_assignment"

    trek_id = db.Column(db.Integer, db.ForeignKey("tm_trek.id"), nullable=False)

    staff_id = db.Column(db.Integer, db.ForeignKey("tm_user.id"), nullable=False)

    assigned_date = db.Column(db.Date)

    status = db.Column(db.String(20), default="Assigned")


class Booking(BaseModel):
    __tablename__ = "tm_booking"

    user_id = db.Column(db.Integer, db.ForeignKey("tm_user.id"), nullable=False)

    trek_id = db.Column(db.Integer, db.ForeignKey("tm_trek.id"), nullable=False)

    booking_date = db.Column(db.Date)

    booking_status = db.Column(db.String(20), default="Booked")

    payment_status = db.Column(db.String(20), default="Pending")

    remarks = db.Column(db.String(500))