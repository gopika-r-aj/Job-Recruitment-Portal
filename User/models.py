from django.db import models
from Company.models import tbl_internship,tbl_placements
from Guest.models import UserRegistration

# Create your models here.

class Internship_Apply(models.Model):
    apply_date=models.DateField(auto_now=True)
    internship=models.ForeignKey(tbl_internship,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)
    intapply_sts=models.IntegerField(default=0)


class Placement_Apply(models.Model):
    apply_date=models.DateField(auto_now=True)
    placement=models.ForeignKey(tbl_placements,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)
    plcapply_sts=models.IntegerField(default=0)
