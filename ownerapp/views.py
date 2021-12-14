from django.shortcuts import render

# Create your views here.
def newfunction(request):
    return render(request,'ologin.html')

def newfunction1(request):
    return render(request,'osignup.html')

def newfunction2(request):
    return render(request,'oprofile.html')  

def newfunction3(request):
    return render(request,'oaddroom.html')

def newfunction4(request):
    return render(request,'list.html')  

def newfunction5(request):
    return render(request,'addhotel.html') 