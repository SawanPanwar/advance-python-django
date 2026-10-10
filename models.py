from django.db import models


class College(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'sos_college'


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    class Meta:
        db_table = 'sos_course'


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_subject'


class Faculty(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    college_id = models.IntegerField()
    college_name = models.CharField(max_length=50)
    subject_id = models.IntegerField()
    subject_name = models.CharField(max_length=50)
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_faculty'


class Marksheet(models.Model):
    roll_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()

    class Meta:
        db_table = 'sos_marksheet'


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    college_id = models.IntegerField()
    college_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_student'
