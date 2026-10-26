from .base_service import BaseService
from ..dao.user_dao import UserDAO
from ..models import User


class UserService(BaseService):

    def get_dao(self):
        return UserDAO()

    def authenticate(self, login_id, password):
        query = User.objects.all()

        query = query.filter(login_id=login_id.strip())
        query = query.filter(password=password.strip())

        if len(query) > 0:
            return query.first()
        else:
            return None
