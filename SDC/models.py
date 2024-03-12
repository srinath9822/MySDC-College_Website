import email
from pickle import TRUE
from re import M
from django.db import models

# Create your models here.

class ourteachers(models.Model):
    tid = models.TextField(primary_key=True)
    tname = models.TextField(max_length=50)
    tmail = models.EmailField(max_length=50)
    class Meta:
        db_table = "ourteachers"



class student(models.Model):
    studentid = models.TextField(primary_key=True)
    studentname = models.TextField(max_length=50)
    studentmail = models.EmailField(max_length=50)
    class Meta:
        db_table = "student"

class registeredstudent(models.Model):
    studentid = models.TextField(primary_key=True)
    studentmail = models.EmailField(max_length=50)
    studentname = models.TextField(max_length=100)
    studentsem= models.TextField(max_length=100)
    studentsec= models.TextField(max_length=100)
    studentpass= models.TextField(max_length=100)
    class Meta:
        db_table = "registeredstudent"

class subjects(models.Model):
    subject = models.TextField(primary_key=True)
    sem = models.IntegerField()
    class Meta:
        db_table = "subjects"

class assignteach(models.Model):
    semester =models.TextField(max_length=10)
    section =models.TextField(max_length=10)
    subjectname =models.TextField(max_length=50)
    teacher =models.TextField(max_length=50)
    class Meta:
        db_table ="assignteach"

class feedback(models.Model):
    regnum=models.TextField(max_length=50)
    semester =models.TextField(max_length=10)
    section =models.TextField(max_length=10)
    subjectname =models.TextField(max_length=50)
    teacher =models.TextField(max_length=50)
    rating =models.TextField(max_length=10)
    suggestion=models.TextField(max_length=200)
    class Meta:
        db_table ="studfeedback"


class registeredteacher(models.Model):
    tid = models.TextField(primary_key=True)
    tmail = models.EmailField(max_length=50)
    tname = models.TextField(max_length=100)
    qualification= models.TextField(max_length=100)
    mobile= models.TextField(max_length=100)
    password= models.TextField(max_length=100)
    class Meta:
        db_table = "registeredteacher"