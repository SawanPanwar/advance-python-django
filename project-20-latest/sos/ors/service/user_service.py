from .base_service import BaseService
from ..dao.user_dao import UserDAO
from ..mail.email_builder import EmailBuilder
from ..mail.email_details import EmailDetails
from ..mail.email_service import EmailService
from ..models import User


class UserService(BaseService):

    def get_dao(self):
        return UserDAO()

    def authenticate(self, login_id, password):
        users = self.get_dao().find_by_unique_key('login_id', login_id)

        user = users.first()

        if user and user.check_password(password):
            return user

        return None

    def register_user(self, obj):
        self.save(obj)

        details = EmailDetails()
        details.to = [obj.login_id]
        details.subject = 'User Registration Successfully !!'
        details.text = EmailBuilder.sign_up(obj)

        EmailService.send(details)
