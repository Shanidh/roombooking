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
    return render(request,'contactus.html')  

def newfunction6(request):
    return render(request,'caresults.html')  

def newfunction7(request):
    return render(request,'admin1.html')  

def newfunction8(request):
    return render(request,'owner.html')                

def newfunction9(request):
    return render(request,'ownerhome.html')  

def newfunction10(request):
    return render(request,'whitehotel.html')    

def newfunction11(request):
    return render(request,'packages.html')   

def newfunction12(request):
    return render(request,'bookingform.html')  

def uchangepass(request):

    uid=request.session['sample']
    obj2=userbooking.objects.get(id=uid)
    try:
        oldpass = request.POST['password']
        newpass = request.POST['newpassword']
        user = request.session['sample']
 
        obj2 = userbooking.objects.get(id=user)
        if obj2.password == oldpass:
            obj2.password = newpass
            obj2.save()
            return render(request, 'index.html', {'msg2': 'password change successfully'})
        return render(request, 'profile.html', {'msg2': 'change password'})

    except Exception as e:
        print(e)
    return render(request,'profile.html',{"msg":obj2})                

def uprofile(request):
    try:
        uid=request.session['sample']
        obj2=userbooking.objects.get(id=uid)
        print(obj2.username)
        
        if request.method == 'POST':
            username = request.POST['upusername']
            email=request.POST['upemail']
            mobnumber=request.POST['upmobile']
            b=userbooking.objects.filter(id=uid).update(username=username,email=email,phone_num=mobnumber)
            b.save()
           
           
            return render(request,'profile.html')
        print(obj2.username)    
        return render(request,'profile.html',{"msg":obj2})

    except Exception as e: print(e)
    return render(request,'profile.html',{"msg":obj2})

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

# def userimage(request):

#      image1=request.FILES['image1']
#      file_name=str(random())+image.name
#      print(file_name)
#      obj1=FileSystemStorage()
#      obj1.save(file_name, image1)
#      obj2=userbooking(image=file_name)
#      obj2.save()
     

#      uid=request.session['sample']
#      seid=userbooking.objects.filter(id=uid).update(image=uid)
     
#      return render(request,'profile.html')  

def newfunction14(request):
    return render(request,'blogs.html')     

def newfunction15(request):
    return render(request,'blogresult.html')    

def newfunction16(request):
    return render(request,'bookreciept.html')   

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