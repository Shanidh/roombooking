from django.shortcuts import render, redirect
from . models import *
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from random import random

# Create your views here.
def newfunction(request):
    try:
        if request.method == "POST":            
            email = request.POST['lemail']
            password = request.POST['lpassword']
            ob1 = owners.objects.get(email=email)
            if ob1.password==password:
                request.session['sample1'] = ob1.id
                return render(request,'afterlogin.html')


    except Exception as e:
        print(e)
    return render(request,'ologin.html',{"msg1": "invalid username or password"})

def newfunction1(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            obj = owners.objects.filter(username=username).exists()
            if(obj == False):
                username = request.POST['username']
                email = request.POST['email']
                dob = request.POST['dob']
                phonenum=request.POST['phone']
                password1 = request.POST['password']
                gender=request.POST['gender']
                obj1 = owners(username=username, email=email,dob=dob, phone_num=phonenum, password=password1, gender=gender)
                obj1.save()
                return render(request, 'osignup.html', {"msg": "saved successfully"})
            else:
                return render(request, 'osignup.html', {"err": "user already exists"})
    except Exception as e:
        print(e)
    return render(request, 'osignup.html')

def ologout(request):
    try:
        del request.session['sample1']
    except KeyError:
        pass 
    return render(request,'ologin.html')    

def newfunction2(request):
    return render(request,'oprofile.html')  

def newfunction4(request):
    return render(request,'list.html')  
    

def addproperty(request):
    # print(request.session['sample1'])  
    try: 
        obj = ownerproperties.objects.all()
        if request.method=='POST':                  
           property_name=request.POST['property_name1']
           property_type=request.POST['property_type']
           star_rate=request.POST['star_rate']
           contact_name=request.POST['contact_name']
           contact_phone=request.POST['contact_phone']
           property_address=request.POST['property_address']
           City=request.POST['City']
           State=request.POST['State']
           Pincode=request.POST['Pincode']
           description=request.POST['description']
           Cancel_freecharge_date=request.POST['Cancel_freecharge_date']
           Children=request.POST['Children']
           pets=request.POST['pets']
           payment=request.POST['payment']
           clientid=request.session['sample1']
           print(clientid)
           propertyimage=request.FILES['propertyimage']  
           file_name = str(random())+propertyimage.name
           print(file_name)
           obj5 = FileSystemStorage()
           obj5.save(file_name, propertyimage)
           obj1=ownerproperties(property_name=property_name,property_type=property_type,star_rate=star_rate,contact_name=contact_name,contact_phone=contact_phone,property_address=property_address,City=City,State=State,Pincode=Pincode,description=description,Cancel_freecharge_date=Cancel_freecharge_date,Children=Children,pets=pets,payment=payment,uploadby=clientid,propertyimage=propertyimage)
           obj1.save()
           return render(request,'afterlogin.html')   
    except Exception as e: print(e)          
    return render(request,'addhotel.html')     


def addroom(request):
    userid=request.session['sample1']
    activeprop = request.session['prprty']
    propertydt=ownerproperties(id=activeprop, uploadby=userid)
    pp=roomproperty.objects.filter(property_id_id=activeprop)
    if request.method=='POST':
        roomnumber=request.POST['roomnumber']
        roomtype=request.POST['roomtype']
        capacity=request.POST['capacity']
        price=request.POST['price']
        status=request.POST['status']
        bb=roomproperty(roomnumber=roomnumber,roomtype=roomtype, capacity=capacity, price=price, status=status,property_id_id=activeprop,owner_id=userid)
        bb.save()
        return render(request,'odashboard.html', {'dataa':pp})   
    return render(request, 'odashboard.html') 

def newfunction6(request,prpid=None):
    userid=request.session['sample1']
    propertydt=ownerproperties(id=prpid, uploadby=userid)
    k=roomproperty.objects.filter(property_id_id=propertydt.id)
    activeprop = request.session['prprty'] = prpid
    print(activeprop)
    return render(request, 'odashboard.html',{'dataa':k})  

def newfunction7(request):
    # if 'sample1' not in request.session:
    #     print("Please login")
    # else:
    return render(request,'afterlogin.html')       

def myproperty(request):
    userid=request.session['sample1']
    obj=ownerproperties.objects.filter(uploadby=userid)
    return render(request,'myproperty.html',{'data':obj})     

def newfunction9(request):
    return render(request,'editroom.html')      

def newfunction10(request):
    return render(request,'viewroom.html')     

def newfunction11(request):
    return render(request,'allbooking.html') 

def facilities(request,prpid=None):
    userid=request.session['sample1']
    propertydt=ownerproperties(id=prpid, uploadby=userid)
    k=roomproperty.objects.filter(property_id_id=propertydt.id)
    activeprop = request.session['prprty'] = prpid
    print(activeprop)
    if request.method=='POST':
        free_wifi=request.POST['free_wifi']
        if free_wifi=="":
            test ="False"
        else:
            test="True"
        
        print(free_wifi)
        # restaurant=request.POST['restaurant']
        # Room_Service=request.POST['Room_Service']
        # Bar=request.POST['Bar']
        # front_desk=request.POST['front_desk']
        # Sauna=request.POST['Sauna']
        # Fitness_Centre=request.POST['Fitness_Centre']
        # Garden=request.POST['Garden']
        # Terrace=request.POST['Terrace']
        # Airport_Shuttle=request.POST['Airport_Shuttle']
        # Family_Rooms=request.POST['Family_Rooms']
        # Spa=request.POST['Spa']
        # Hot_Tub=request.POST['Hot_Tub']
        # Air_Conditioning=request.POST['Air_Conditioning']
        # Water_Park=request.POST['Water_Park']
        # ElectricVehicleChargingStations=request.POST['ElectricVehicleChargingStations']
        # Swimming_Pool=request.POST['Swimming_Pool']
        bb=facilities(free_wifi=free_wifi,restaurant=restaurant, Room_Service=Room_Service, Bar=Bar, front_desk=front_desk,Sauna=Sauna,Fitness_Centre=Fitness_Centre,Garden=Garden,Terrace=Terrace,Airport_Shuttle=Airport_Shuttle,Family_Rooms=Family_Rooms,Spa=Spa,Hot_Tub=Hot_Tub,Air_Conditioning=Air_Conditioning,Water_Park=Water_Park,ElectricVehicleChargingStations=ElectricVehicleChargingStations,Swimming_Pool=Swimming_Pool,owner_id=userid,propertyf_id=activeprop)
        bb.save()
        return render(request,'myproperty.html')
    return render(request,'facilities.html')          