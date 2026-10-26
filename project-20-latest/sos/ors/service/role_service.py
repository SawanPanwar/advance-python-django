from ..dao.role_dao import RoleDAO
from ..service.base_service import BaseService


class RoleService(BaseService):

    def get_dao(self):
        return RoleDAO()