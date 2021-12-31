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
                obj1 = owners(username=username, email=email,dob=dob, phone_num=phonenum, password=password1)
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

def newfunction5(request):
    return render(request,'addhotel.html') 

def newfunction6(request):
    return render(request,'odashboard.html')  

def newfunction7(request):
    return render(request,'afterlogin.html')       

def newfunction8(request):
    return render(request,'myproperty.html')      

def newfunction9(request):
    return render(request,'editroom.html')      

def newfunction10(request):
    return render(request,'viewroom.html')     

def newfunction11(request):
    return render(request,'allbooking.html')       