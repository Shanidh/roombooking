from django.db import models

# Create your models here.
class owners(models.Model):
    id=models.BigAutoField(primary_key=True)
    username=models.CharField(max_length=25)
    email=models.EmailField()
    dob=models.DateField()
    phone_num=models.BigIntegerField()
    password=models.CharField(max_length=10)
    gender=models.CharField(max_length=20,null=True)

class facilities(models.Model):
    id=models.BigAutoField(primary_key=True)
    free_wifi=models.CharField(max_length=6,null=True)
    restaurant=models.CharField(max_length=6,null=True)
    Room_Service=models.CharField(max_length=6,null=True)
    Bar=models.CharField(max_length=6,null=True)
    front_desk=models.CharField(max_length=6,null=True)
    Sauna=models.CharField(max_length=6,null=True)
    Fitness_Centre=models.CharField(max_length=6,null=True)
    Garden=models.CharField(max_length=6,null=True)
    Terrace=models.CharField(max_length=6,null=True)
    Airport_Shuttle=models.CharField(max_length=6,null=True)
    Family_Rooms=models.CharField(max_length=6,null=True)
    Spa=models.CharField(max_length=6,null=True)
    Hot_Tub=models.CharField(max_length=6,null=True)
    Air_Conditioning=models.CharField(max_length=6,null=True)
    Water_Park=models.CharField(max_length=6,null=True)
    ElectricVehicleChargingStations=models.CharField(max_length=6,null=True)
    Swimming_Pool=models.CharField(max_length=6,null=True)    

class ownerproperties(models.Model):
    id=models.BigAutoField(primary_key=True)
    uploadby=models.CharField(max_length=6,null=True)    
    property_name=models.CharField(max_length=50)
    property_type=models.CharField(max_length=20,null=True)
    star_rate=models.CharField(max_length=20,null=True)
    contact_name=models.CharField(max_length=50)
    contact_phone=models.BigIntegerField()
    property_address=models.CharField(max_length=100)
    City=models.CharField(max_length=20,null=True)
    State=models.CharField(max_length=20,null=True)
    Pincode=models.CharField(max_length=6)
    description=models.CharField(max_length=500)
    Facilities=models.ForeignKey(facilities,on_delete=models.CASCADE,null=True)
    Cancel_freecharge_date=models.CharField(max_length=20,null=True)
    Children=models.CharField(max_length=20,null=True)
    pets=models.CharField(max_length=20,null=True)
    payment=models.CharField(max_length=20,null=True)

