from django.db import models
from Guest.models import CompanyRegistration

# Create your models here.

class tbl_internship(models.Model):
    int_title=models.CharField(max_length=50)
    int_post=models.CharField(max_length=50)
    int_date=models.DateField(auto_now=True)
    int_duration=models.CharField(max_length=50)
    int_details=models.TextField(null=True)
    int_stipend=models.IntegerField(default=0)
    company=models.ForeignKey(CompanyRegistration,on_delete=models.SET_NULL,null=True)

class tbl_placements(models.Model):
    plc_title=models.CharField(max_length=50)
    plc_designation=models.CharField(max_length=50)
    plc_date=models.DateField(auto_now=True)
    plc_salary=models.IntegerField(default=0)
    plc_details=models.TextField(null=True)
    company=models.ForeignKey(CompanyRegistration,on_delete=models.SET_NULL,null=True)
   