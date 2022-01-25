from django.shortcuts import render
from . models import *
from ownerapp.models import *
from bookingapp.models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from random import random

# Create your views here.
def adlogin(request):
    try:
        if request.method == "POST":            
            email = request.POST['aemail']
            password = request.POST['apassword']
            ob1 = admin1.objects.get(email=email)
            if ob1.password==password:
                request.session['sample3'] = ob1.id
                print(ob1.id)
                return render(request,'admindashboard.html')


    except Exception as e:
        print(e)
    return render(request,'alogin.html')

def asignup(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            username = request.POST['username']
            email = request.POST['email']
            dob = request.POST['dob']
            phonenum=request.POST['phone']
            password1 = request.POST['password']
            gender=request.POST['gender']
            obj1 = admin1(username=username, email=email,dob=dob, phone_num=phonenum, password=password1, gender=gender)
            obj1.save()
            return render(request, 'asignup.html', {"msg": "saved successfully"})
    except Exception as e: print(e)
    return render(request,'asignup.html')    

def alogout(request):
    try:
        del request.session['sample3']
    except KeyError:
        pass
    return render(request,'alogin.html')

def admindb(request):
       properties=ownerproperties.objects.all()
       ownersli=owners.objects.filter()
       custs=userbooking.objects.filter()
       totalp=len(properties)
       totalo=len(ownersli)
       totalc=len(custs)
       propt={'prop':properties,'totalp':totalp,'totalo':totalo,'totalc':totalc}
       return render(request,'admindashboard.html',propt)
       

def adminviewppt(request,propvid=None):
    propt=ownerproperties.objects.filter(id=propvid)
    roomm=roomproperty.objects.filter(property_id_id=propvid)
    context={'propt':propt,'roomt':roomm}
    return render(request,'viewproperty.html',context)         

def ownerss(request):
    propp=owners.objects.all()
    return render(request,'ownerss.html',{'propp':propp})   

def editowners(request):
    return render(request,'editowners.html')           

def addowners(request):
    return render(request,'addowners.html')     

def customers(request):
    cust=userbooking.objects.all()
    return render(request,'customers.html',{'cust':cust})         

def settings(request):
    try:
      adid=request.session['sample3']
      obj12=admin1.objects.filter(id=adid)
      return render(request,'settings.html',{'adm':obj12})  
    except Exception as e: print(e)
    return render(request,'admindashboard.html')       

def booking(request):
    b=bookform.objects.all()
    return render(request,'booking.html',{'b':b})       

def ablogs(request):
    blog=blogs.objects.all()
    return render(request,'ablogs.html',{'blog':blog})   

def editblog(request,blid=None):
    eblog=blogs.objects.filter(id=blid)
    activeblog = request.session['blogss'] = blid
    return render(request,'editblog.html',{'eblog':eblog})     

def feedbacks(request):
    ocs=ownercontactus.objects.all()
    ccs=usercontactus.objects.all()
    context={'ocs':ocs,'ccs':ccs}
    return render(request,'feedbacks.html',context)     

def upadmin(request):
    try:
        adid=request.session['sample3']
        obj2=admin1.objects.filter(id=adid)
        if request.method=='POST':
            auname=request.POST['auname']
            aemail=request.POST['aemail']
            aphone=request.POST['aphone']
            obj=admin1.objects.filter(id=adid).update(username=auname,email=aemail,phone_num=aphone)
            obj.save()
            messages.success(request, 'Profile Updated')
            return render(request,'settings.html',{'adm':obj2})
    except Exception as e: print(e) 
    messages.error(request, 'Profile Updated')  
    return render(request,'settings.html',{'adm':obj2})   

def changepass(request):
    try:
        adid=request.session['sample3']
        obj2=admin1.objects.filter(id=adid)
        if request.method=='POST':
            password=request.POST['password']
            obj=admin1.objects.filter(id=adid).update(password=password)
            obj.save()
            messages.success(request, 'Password Updated')
            return render(request,'settings.html',{'adm':obj2})
    except Exception as e: print(e)
    messages.error(request, 'Password Updated') 
    return render(request,'settings.html',{'adm':obj2})     

def upimage(request):
    try:
        adid=request.session['sample3']
        obj2=admin1.objects.filter(id=adid)
        if request.method=='POST':
            image1 = request.FILES['image1']
            file_name = str(random())+image1.name
            obj1 = FileSystemStorage()
            obj1.save(file_name, image1)
            obj2 = admin1.objects.filter(id=adid).update(image=file_name)
            obj2.save()
            return render(request,'settings.html',{'adm':obj2})
    except Exception as e: print(e)    
    return render(request,'settings.html',{'adm':obj2})    

def deleteprop(request,propid=None):
    properties=ownerproperties.objects.all()
    ownersli=owners.objects.filter()
    custs=userbooking.objects.filter()
    propdt=ownerproperties.objects.filter(id=propid).delete()
    messages.success(request,'Deleted')
    totalp=len(properties)
    totalo=len(ownersli)
    totalc=len(custs)
    propt={'prop':properties,'totalp':totalp,'totalo':totalo,'totalc':totalc}
    return render(request,'admindashboard.html',propt)  

def deleteown(request,ownid=None):
    propp=owners.objects.all()
    owns=owners.objects.filter(id=ownid).delete()
    messages.success(request,'Deleted Successfully')
    return render(request,'ownerss.html',{'propp':propp})      

def addowner(request):
    propp=owners.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        dob=request.POST['dob']
        obj=owners(username=name,email=email,dob=dob,phone_num=phone,gender=gender)
        obj.save()
        messages.success(request,'Added Successfully')
        return render(request,'ownerss.html',{'propp':propp})
    return render(request,'ownerss.html',{'propp':propp})  

def deletecust(request,custid=None):
    cust=userbooking.objects.all()
    userbooking.objects.filter(id=custid).delete()
    messages.success(request,'Deleted Successfully')
    return render(request,'customers.html',{'cust':cust})       

def delofb(request,ofbid=None):
    ocs=ownercontactus.objects.all()
    ccs=usercontactus.objects.all()
    context={'ocs':ocs,'ccs':ccs}
    ownercontactus.objects.filter(id=ofbid).delete()
    messages.success(request,'Deleted Successfully')
    return render(request,'feedbacks.html',context)   

def delcfb(request,cfbid=None):
    ocs=ownercontactus.objects.all()
    ccs=usercontactus.objects.all()
    context={'ocs':ocs,'ccs':ccs}
    usercontactus.objects.filter(id=cfbid).delete()
    messages.success(request,'Deleted Successfully')
    return render(request,'feedbacks.html',context)                   

def addblog(request):
    return render(request,'addblog.html')  

def addedblog(request):
    try:
        blog=blogs.objects.all()
        if request.method=='POST':
            title=request.POST['title']
            categories=request.POST['categories']
            writtenby=request.POST['writtenby']
            description=request.POST['description']
            # images = request.FILES['images']
            # file_name = str(random())+images.name
            # obj1 = FileSystemStorage()
            # obj1.save(file_name, images)
            obj2=blogs(title=title,categories=categories,writtenby=writtenby,description=description)
            obj2.save()
            messages.success(request,'Added Successfully')
            return render(request,'ablogs.html',{'blog':blog})
    except Exception as e: print(e)    
    return render(request,'addblog.html')     

def editedblog(request):
    blog=blogs.objects.all()
    act = request.session['blogss'] 
    if request.method=='POST':
            title=request.POST['title']
            categories=request.POST['categories']
            writtenby=request.POST['writtenby']
            description=request.POST['description']
            obj2=blogs.objects.filter(id=act).update(title=title,categories=categories,writtenby=writtenby,description=description)
            obj2.save()
            messages.success(request,'Edited Successfully')
    return render(request,'ablogs.html',{'blog':blog})      

def delblog(request,delbid=None):
    blog=blogs.objects.all()
    blogs.objects.filter(id=delbid).delete()
    messages.success(request,'Deleted successfully')
    return render(request,'ablogs.html',{'blog':blog})    

def delbk(request,delbkid=None):
    b=bookform.objects.all()
    bd=bookform.objects.filter(id=delbkid).delete()
    messages.success(request,'Deleted booking')
    return render(request,'booking.html',{'b':b})    