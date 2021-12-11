
from django.urls import path, include
from.import views

urlpatterns = [
    
    path('index',views.newfunction,name='index'),
    path('signup',views.newfunction2,name='signup'),
    path('addroom',views.newfunction3,name='addroom'),
    path('aboutus',views.newfunction4,name='aboutus'),
    path('contactus',views.newfunction5,name='contactus'),
    path('caresults',views.newfunction6,name='caresults'),
    path('admin1',views.newfunction7,name='admin1'),
    path('owner',views.newfunction8,name='owner'),
    path('ownerhome',views.newfunction9,name='ownerhome'),
    path('whitehotel',views.newfunction10,name='whitehotel'),
    path('packages',views.newfunction11,name='packages'),
    path('bookingform',views.newfunction12,name='bookingform'),
]