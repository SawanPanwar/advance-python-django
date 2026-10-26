from abc import ABC, abstractmethod


class BaseService(ABC):

    def save(self, obj):
        return self.get_dao().save(obj)


    def get(self, pk):
        return self.get_dao().get(pk)

    def delete(self, id):
        return self.get_dao().delete(id)

    def search(self, params):
        return self.get_dao().search(params)

    @abstractmethod
    def get_dao(self):
        pass
