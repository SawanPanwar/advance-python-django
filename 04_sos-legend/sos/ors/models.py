from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login_id = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_user'


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = "sos_role"