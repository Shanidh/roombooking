
from django.urls import path, include
from.import views

urlpatterns = [
    
    path('index/',views.usersignup,name='index'),
    path('login/',views.ulogin,name='login'),
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
    path('profile/',views.uchangepass,name='profile'),
    path('blogs',views.newfunction14,name='blogs'),
    path('blogresult',views.newfunction15,name='blogresult'),
    path('bookreciept',views.newfunction16,name='bookreciept'),
    path('reviews',views.newfunction17,name='reviews'),
    path('logout',views.ulogout,name='logout'),
    path('uprofile/',views.uprofile,name='uprofile')
]
