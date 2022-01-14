from django.shortcuts import render
from . models import *

# Create your views here.
def newfunction(request):
    try:
        if request.method == "POST":

            print('hiiiiiii')
            
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
    clid=request.session['sample1']
    print(clid)
    return render(request,'oprofile.html')  

def newfunction4(request):
    return render(request,'list.html')  

def addproperty(request):
    if request.method=='POST':
        property_name=request.POST['property_name']
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
        obj1=ownerproperties(property_name=property_name,property_type=property_type,star_rate=star_rate,contact_name=contact_name,contact_phone=contact_phone,property_address=property_address,City=City,State=State,Pincode=Pincode,description=description,Cancel_freecharge_date=Cancel_freecharge_date,Children=Children,pets=pets,payment=payment,uploadby=clientid)
        obj1.save()
        return render(request,'myproperty.html',{"msg1":"insert successfully"})
    return render(request,'addhotel.html')     

def newfunction6(request):
    return render(request,'odashboard.html')  

def newfunction7(request):
    if 'sample1' not in request.session:
        print("Please login")
    else:
        return render(request,'afterlogin.html')       

def newfunction8(request):
    return render(request,'myproperty.html')      

def newfunction9(request):
    return render(request,'editroom.html')      

def newfunction10(request):
    return render(request,'viewroom.html')     

def newfunction11(request):
    return render(request,'allbooking.html')       