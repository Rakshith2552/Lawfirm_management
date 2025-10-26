from django.db import models
from django.contrib.auth.models import User
from lawfirmapp.models import Appointment,AdvocateProfile


class ModelName(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    #addition fields
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    profile_pic=models.ImageField(upload_to='userimg/',blank=True,null=True)
    
class CaseManagement(models.Model):
    case_type=models.ForeignKey(Appointment,related_name='Appointments',on_delete=models.CASCADE)
    lawyer=models.ForeignKey(AdvocateProfile,related_name='AdvocateProfiles',on_delete=models.CASCADE)
    date=models.DateField()
    Time=models.TimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    



    
    
