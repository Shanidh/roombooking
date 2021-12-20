from django.shortcuts import render

# Create your views here.
def adlogin(request):
    return render(request,'alogin.html')

def admindb(request):
    return render(request,'admindashboard.html')  

def admineditppt(request):
    return render(request,'editproperty.html')         

def owners(request):
    return render(request,'owners.html')   

def editowners(request):
    return render(request,'editowners.html')           

def addowners(request):
    return render(request,'addowners.html')     

def customers(request):
    return render(request,'customers.html')         

def settings(request):
    return render(request,'settings.html')         

def booking(request):
    return render(request,'booking.html')       

def ablogs(request):
    return render(request,'ablogs.html')   

def editblog(request):
    return render(request,'editblog.html')     

def feedbacks(request):
    return render(request,'feedbacks.html')              