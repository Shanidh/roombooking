from django.db import models

# Create your models here.
class admin1(models.Model):
    id=models.BigAutoField(primary_key=True)
    username=models.CharField(max_length=25)
    email=models.EmailField()
    dob=models.DateField()
    phone_num=models.BigIntegerField()
    password=models.CharField(max_length=10)
    gender=models.CharField(max_length=20,null=True)
    image=models.CharField(max_length=2000,null=True)

class blogs(models.Model):
    id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=200)
    categories=models.CharField(max_length=30)
    writtenby=models.CharField(max_length=50)
    image=models.CharField(max_length=400,null=True)
    description=models.CharField(max_length=2000)    