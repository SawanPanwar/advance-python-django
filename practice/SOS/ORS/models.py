from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def to_json(self):
        data = {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'loginId': self.loginId,
            'password': self.password
        }
        return data
    class Meta:
        db_table = "SOS_USER"