from ..models import User
from ..utility.DataValidator import DataValidator
from .BaseService import BaseService


class ForgetPasswordService(BaseService):

    def search(self, params):
        val = params.get('loginId', None)
        q = self.get_model().objects.filter()
        if (DataValidator.isNotNull(val)):
            q = q.filter(loginId=val)
        return q

    def get_model(self):
        return User
