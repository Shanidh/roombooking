from django.db import models

# Create your models here.
class userbooking(models.Model):
    id=models.BigAutoField(primary_key=True)
    username=models.CharField(max_length=25)
    email=models.EmailField()
    dob=models.DateField(null=True, blank=True)
    phone_num=models.BigIntegerField(null=True)
    password=models.CharField(max_length=10)
    gender=models.CharField(max_length=20,null=True)
    image=models.CharField(max_length=500, null=True) 

class usercontactus(models.Model):
    user=models.ForeignKey(userbooking,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.CharField(max_length=20,null=True)
    message=models.CharField(max_length=200,null=True)    