from django.urls import path, include
from.import views

urlpatterns = [

    path('ologin/',views.newfunction,name='ologin'),
    path('osignup/',views.newfunction1,name='osignup'),
    path('oprofile',views.newfunction2,name='oprofile'),
    path('list/',views.newfunction4,name='list'),
    path('addhotel',views.newfunction5,name='addhotel'),
    path('odashboard/',views.newfunction6,name='odashboard'),
    path('afterlogin',views.newfunction7,name='afterlogin'),
    path('myproperty',views.newfunction8,name='myproperty'),
    path('editroom',views.newfunction9,name='editroom'),
    path('viewroom',views.newfunction10,name='viewroom'),
    path('allbooking',views.newfunction11,name='allbooking'),
    path('ologout/',views.ologout,name='ologout'),
]