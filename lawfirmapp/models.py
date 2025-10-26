from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class AdvocateProfile(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    name=models.CharField(max_length=100)
    email=models.EmailField()
    year_of_exp=models.PositiveIntegerField()
    specialization=models.CharField(max_length=255)
    total_cases=models.PositiveIntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='advimg/',blank=True,null=True)

class AllCases(models.Model):
    case_title=models.CharField(max_length=100)
    case_description=models.TextField()
    case_image=models.ImageField(upload_to='caseimg/',blank=True,null=True)


case_types=[
    ('criminal','CRIMINAL'),
    ('civil','CIVIL'),
    ('labour law','LABOUR LAW'),
    ('tax law','TAX LAW'),
    ('other','OTHER') 
]

class Enquriy(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    image=models.ImageField()
    description=models.TextField()
    case_type=models.CharField(max_length=100,choices=case_types,default='TAX LAW')
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    case_type=models.CharField(max_length=100,choices=case_types,default='TAX LAW')
    description=models.TextField()
    case_document=models.ImageField(upload_to='caseimg/',blank=True,null=True)
    total_no_hearings=models.IntegerField()
    court_name=models.CharField(max_length=100)
    fee=models.IntegerField(default=500)