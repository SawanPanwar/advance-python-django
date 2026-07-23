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
    __tablename__ = "ors_user"

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    login_id = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date)
    address = db.Column(db.String(50))
    gender = db.Column(db.String(50), default="")
    role_id = db.Column(db.Integer)
    role_name = db.Column(db.String(50))

    def get_key(self):
        return self.id

    def get_value(self):
        return f"{self.first_name} {self.last_name}"


class Role(BaseModel, DropdownItem):
    __tablename__ = "ors_role"

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))

    def get_key(self):
        return self.id

    def get_value(self):
        return self.name
