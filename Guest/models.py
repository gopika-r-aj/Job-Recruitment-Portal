from django.db import models
from Admin.models import *

# Create your models here.


class UserRegistration(models.Model):
    user_name=models.CharField(max_length=100)
    user_contact=models.CharField(max_length=100)
    user_email=models.EmailField(unique=True)
    user_gender=models.CharField(max_length=100)
    user_address=models.TextField(null=True)
    user_course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    user_photo=models.FileField(upload_to='userdocs/')
    user_proof=models.FileField(upload_to='userdocs/')
    user_password=models.CharField(max_length=100,unique=True)
    place=models.ForeignKey(Place,on_delete=models.CASCADE) 
    user_doj=models.DateField(auto_now=True)
    user_graduation=models.CharField(max_length=50)
    user_vsts=models.IntegerField(default=0)


class CompanyRegistration(models.Model):
    company_name=models.CharField(max_length=100)
    company_contact=models.CharField(max_length=100)
    company_email=models.EmailField(unique=True)
    company_address=models.TextField(null=True)
    company_logo=models.FileField(upload_to='companydocs/')
    company_proof=models.FileField(upload_to='companydocs/')
    company_password=models.CharField(max_length=100,unique=True)
    place=models.ForeignKey(Place,on_delete=models.CASCADE) 
    company_vsts=models.IntegerField(default=0)
    