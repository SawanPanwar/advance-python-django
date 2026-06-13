from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_user'


class Marksheet(models.Model):
    rollNo = models.IntegerField(max_length=20)
    name = models.CharField(max_length=30)
    physics = models.FloatField(max_length=3)
    chemistry = models.FloatField(max_length=3)
    maths = models.FloatField(max_length=3)

    class Meta:
        db_table = "sos_marksheet"
