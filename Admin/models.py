from django.db import models

# Create your models here.

class Admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.EmailField(unique=True)
    admin_password=models.CharField(max_length=50,unique=True)

class Department(models.Model):
    department_name=models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class Course(models.Model):    
    course_name=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.course_name

class District(models.Model):
    district_name=models.CharField(max_length=50)

    def __str__(self):
        return self.district_name

class Place(models.Model):
    place_name=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.place_name 

class Designation(models.Model):
    designation_name=models.CharField(max_length=50)

    def __str__(self):
        return self.designation_name




    