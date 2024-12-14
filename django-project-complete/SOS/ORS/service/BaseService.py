from abc import ABC, abstractmethod


class BaseService(ABC):

    def __init__(self):
        self.pageSize = 5

    def save(self, obj):
        if (obj.id == 0):
            obj.id = None
        obj.save()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        obj.delete()

    def get(self, obj_id):
        try:
            obj = self.get_model().objects.get(id=obj_id)
            return obj
        except self.get_model().DoesNotExist:
            return None

    def search(self):
        try:
            objs = self.get_model().objects.all()
            return objs
        except self.get_model().DoesNotExist:
            return None

    def preload(self):
        try:
            objs = self.get_model().objects.all()
            return objs
        except self.get_model().DoesNotExist:
            return None

    @abstractmethod
    def get_model(self):
        pass
