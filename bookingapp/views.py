from django.shortcuts import render
from django.urls import reverse
from . models import *
from django.http import HttpResponse
from random import random
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from adminapp.models import *
from ownerapp.models import *


# Create your views here.

def usersignup(request):
    try:
        if request.method == 'POST':
            uname = request.POST['username']
            obj = userbooking.objects.filter(username=uname).exists()

            if obj==True:
                   return JsonResponse({"msg2":"user already exists"})
                
            else:
                uname = request.POST['username']
                email = request.POST['email']
                dob = request.POST['dob']
                phone=request.POST['phone']
                password=request.POST['password']
                gender=request.POST['gender']
                obj1 = userbooking(username=uname, email=email,dob=dob, phone_num=phone, password=password, gender=gender)
                obj1.save()
                
                # return JsonResponse({"msg2":"saved successfully"})
                return render(request,'index.html')       
    except Exception as e:print(e)
    return render(request,'index.html')    

def ulogin(request):
    try:
        if request.method == "POST":
            email = request.POST['uuemail']
            password = request.POST['upassword']
            obj2 = userbooking.objects.get(email=email)
            if obj2.password==password:
                request.session['sample'] = obj2.id
                return render(request,'index.html')

    except Exception as e:
        print(e)
    return render(request,'index.html')  


def ulogout(request):
    try:
        del request.session['sample']
    except KeyError:
        pass    
    return render(request,'index.html')    


def userindex(request):
    return render(request,'index.html')      
    
def newfunction3(request):
    return render(request,'addroom.html')   

def newfunction4(request):
    return render(request,'aboutus.html')    

def newfunction5(request):
    adc=admin1.objects.all()
    return render(request,'contactus.html',{'adc':adc})  

def newfunction6(request):
    ownerproperties.objects.all()
    if request.method=='POST':
        City=request.POST['City']
        propss=ownerproperties.objects.filter(City=City)
        return render(request,'caresults.html',{'propss':propss})  
    messages.error(request,'Not Found')    
    return render(request,'caresults.html')    

def newfunction7(request):
    return render(request,'admin1.html')  

def newfunction8(request):
    return render(request,'owner.html')                

def newfunction9(request):
    return render(request,'ownerhome.html')  

def newfunction10(request,prppid=None):
    pr=ownerproperties.objects.filter(id=prppid)
    actpropty=request.session['propty']=prppid
    rr=roomproperty.objects.filter(property_id_id=prppid,status="Available")
    context={'pr':pr,'rr':rr}
    return render(request,'whitehotel.html',context)    

def newfunction11(request):
    return render(request,'packages.html')   

def newfunction12(request,bfid=None):
    actbform=request.session['bform'] = bfid
    prppp=roomproperty.objects.filter(id=actbform)
    actpropty=request.session['propty']
    prpty=ownerproperties.objects.filter(id=actpropty)
    context={'prppp':prppp,'prpty':prpty}
    return render(request,'bookingform.html',context)  

def uchangepass(request):

    uid=request.session['sample']
    obj2=userbooking.objects.get(id=uid)
    us=userbooking.objects.filter(id=uid)
    ub=bookform.objects.filter(userss_id=uid)
    msg={'us':us,'ub':ub}
    try:
        oldpass = request.POST['password']
        newpass = request.POST['newpassword']
        user = request.session['sample']
 
        obj2 = userbooking.objects.get(id=user)
        if obj2.password == oldpass:
            obj2.password = newpass
            obj2.save()
            messages.success(request,'Password Changed Successfully')
            return render(request, 'profile.html', msg)
        return render(request, 'profile.html', msg)

    except Exception as e:print(e)
    messages.error(request,'Password not changed')
    return render(request,'profile.html',msg)                

def uprofile(request):
    try:
        uid=request.session['sample']
        obj2=userbooking.objects.get(id=uid)
        us=userbooking.objects.filter(id=uid)
        ub=bookform.objects.filter(userss_id=uid)
        msg={'us':us,'ub':ub}
        print(obj2.username)
        
        if request.method == 'POST':
            username = request.POST['upusername']
            email=request.POST['upemail']
            mobnumber=request.POST['upmobile']
            b=userbooking.objects.filter(id=uid).update(username=username,email=email,phone_num=mobnumber)
            b.save()
           
           
            return render(request,'profile.html')
        print(obj2.username)    
        return render(request,'profile.html',msg)

    except Exception as e: print(e)
    return render(request,'profile.html',msg)

def userimage(request):
    try:
        obj3 = userbooking.objects.all()
        if request.method=='POST':
            userid =  request.session['sample']
            image1 = request.FILES['image1']
            file_name = str(random())+image1.name
            obj1 = FileSystemStorage()
            obj1.save(file_name, image1)
            userprof = userbooking.objects.filter(id=userid).update(image= file_name)
            userprof.save()
        
    except Exception as e:
        print(e)
    
    return render(request, 'index.html', {"pas": obj3})   

 

def newfunction14(request):
    bl=blogs.objects.all()
    return render(request,'blogs.html',{'bl':bl})     

def newfunction15(request):
    return render(request,'blogresult.html')    

def newfunction16(request,brid=None):
    brr=bookform.objects.filter(id=brid)
    return render(request,'bookreciept.html',{'brr':brr})   

def newfunction17(request):
    return render(request,'reviews.html')   
   
def usersendmessage(request):
    try:
       userid=request.session['sample']
       if request.method=='POST':
           message=request.POST['message']
           name=request.POST['name']
           email=request.POST['email']
           subject=request.POST['subject']
           obj=usercontactus(message=message,name=name,email=email,subject=subject,user_id=userid)
           obj.save()
           messages.success(request, 'Message sended successfully.')
           return render(request,'contactus.html')
    except Exception as e: print(e)       
    messages.error(request, 'Message not sended')
    return render(request,'contactus.html')  

def bform(request):
    actbform=request.session['bform']
    prppp=roomproperty.objects.filter(id=actbform)
    userid=request.session['sample']
    actpropty=request.session['propty']
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        checkin=request.POST['checkin']
        checkout=request.POST['checkout']
        address=request.POST['address']
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        pincode=request.POST['pincode']
        phone=request.POST['phone']
        email=request.POST['email']
        obj=bookform(fname=fname,lname=lname,checkin=checkin,checkout=checkout,address=address,country=country,state=state,city=city,pincode=pincode,phone=phone,email=email,roomid=actbform,userss_id=userid,propertyid=actpropty)
        obj.save()
        messages.success(request,'Booked successfully')
        return render(request,'index.html')
    return render(request,'bookingform.html')  

def profile(request):
    uid=request.session['sample']    
    
    us=userbooking.objects.filter(id=uid)
    ub=bookform.objects.filter(userss_id=uid)
    pp=ownerproperties.objects.get()
    msg={'us':us,'ub':ub}
    return render(request,'profile.html',msg)         

def cancelbook(request,cbid=None): 
    us=userbooking.objects.filter(id=uid)
    ub=bookform.objects.filter(userss_id=uid) 
    msg={'us':us,'ub':ub}
    booform.objects.filter(id=cbid).delete()
    mesages.success(request,'Cancelled booking')
    return render(request,'profile.html',msg)   

def hotels(request):
    if request.method=='POST':
      propss=ownerproperties.objects.filter(property_type="Hotel")
      return render(request,'caresults.html',{'propss':propss}) 
    messages.error(request,'Not found')  
    return render(request,'caresults.html')      

def Resorts(request):
    if request.method=='POST':
      propss=ownerproperties.objects.filter(property_type="Resort")
      return render(request,'caresults.html',{'propss':propss}) 
    messages.error(request,'Not found')  
    return render(request,'caresults.html') 

def Hostels(request):
    if request.method=='POST':
      propss=ownerproperties.objects.filter(property_type="Hostel")
      return render(request,'caresults.html',{'propss':propss}) 
    messages.error(request,'Not found')  
    return render(request,'caresults.html') 

def Apartments(request):
    if request.method=='POST':
      propss=ownerproperties.objects.filter(property_type="Apartment")
      return render(request,'caresults.html',{'propss':propss}) 
    messages.error(request,'Not found')  
    return render(request,'caresults.html') 

def Homestays(request):
    if request.method=='POST':
      propss=ownerproperties.objects.filter(property_type="Homestay")
      return render(request,'caresults.html',{'propss':propss}) 
    messages.error(request,'Not found')  
    return render(request,'caresults.html') 

def Boats(request):
    if request.method=='POST':
      propss=ownerproperties.objects.filter(property_type="Houseboat")
      return render(request,'caresults.html',{'propss':propss}) 
    messages.error(request,'Not found')  
    return render(request,'caresults.html') 

def Others(request):
    if request.method=='POST':
      propss=ownerproperties.objects.filter(property_type="Others")
      return render(request,'caresults.html',{'propss':propss}) 
    messages.error(request,'Not found')  
    return render(request,'caresults.html')                            