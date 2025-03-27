from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.EmailField()
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20, default='')
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=50, default='')
    mobileNumber = models.CharField(max_length=50, default='')
    roleId = models.IntegerField()
    roleName = models.CharField(max_length=50)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        db_table = 'sos_user'


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.name

    class Meta:
        db_table = 'sos_role'


class Marksheet(models.Model):
    rollNumber = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()

    class Meta:
        db_table = 'sos_marksheet'
