
from django.urls import path, include
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.userindex,name='index'),
    path('signup/',views.usersignup,name='signup'),
    path('login/',views.ulogin,name='login'),
    # path('signup',views.newfunction2,name='signup'),
    path('addroom',views.newfunction3,name='addroom'),
    path('aboutus',views.newfunction4,name='aboutus'),
    path('contactus',views.newfunction5,name='contactus'),
    path('caresults',views.newfunction6,name='caresults'),
    path('admin1',views.newfunction7,name='admin1'),
    path('owner',views.newfunction8,name='owner'),
    path('ownerhome',views.newfunction9,name='ownerhome'),
    path('whitehotel/<int:prppid>/',views.newfunction10,name='whitehotel'),
    path('packages',views.newfunction11,name='packages'),
    path('bookingform/<int:bfid>/',views.newfunction12,name='bookingform'),
    path('changepass/',views.uchangepass,name='changepass'),
    path('blogs',views.newfunction14,name='blogs'),
    path('blogresult',views.newfunction15,name='blogresult'),
    path('bookreciept/<int:brid>/',views.newfunction16,name='bookreciept'),
    path('reviews',views.newfunction17,name='reviews'),
    path('logout',views.ulogout,name='logout'),
    path('uprofile/',views.uprofile,name='uprofile'),
    path('userimage/',views.userimage,name='userimage'),
    path('usersendmessage/',views.usersendmessage,name='usersendmessage'),
    path('bform/',views.bform,name='bform'),
    path('profile/',views.profile,name='profile'),
    path('cancelbook/<int:cbid>/',views.cancelbook,name='cancelbook'),
    path('hotels',views.hotels,name='hotels'),
    path('Resorts',views.Resorts,name='Resorts'),
    path('Hostels',views.Hostels,name='Hostels'),
    path('Apartments',views.Apartments,name='Apartments'),
    path('Homestays',views.Homestays,name='Homestays'),
    path('Boats',views.Boats,name='Boats'),
    path('Others',views.Others,name='Others'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)