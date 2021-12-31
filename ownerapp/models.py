from django.db import models

# Create your models here.
class owners(models.Model):
    username=models.CharField(max_length=25)
    email=models.EmailField()
    dob=models.DateField()
    phone_num=models.BigIntegerField()
    password=models.CharField(max_length=10)