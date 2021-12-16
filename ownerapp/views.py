from django.shortcuts import render

# Create your views here.
def newfunction(request):
    return render(request,'ologin.html')

def newfunction1(request):
    return render(request,'osignup.html')

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