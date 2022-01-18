from django.urls import path, include
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('ologin/',views.newfunction,name='ologin'),
    path('osignup/',views.newfunction1,name='osignup'),
    path('oprofile',views.newfunction2,name='oprofile'),
    path('list/',views.newfunction4,name='list'),
    path('addhotel',views.addproperty,name='addhotel'),
    path('odashboard/<int:prpid>/',views.newfunction6,name='odashboard'),
    # path('odashboard/',views.newfunction6,name='odashboard'),
    path('afterlogin',views.newfunction7,name='afterlogin'),
    path('myproperty/',views.myproperty,name='myproperty'),
    path('editroom',views.newfunction9,name='editroom'),
    path('viewroom',views.newfunction10,name='viewroom'),
    path('allbooking',views.newfunction11,name='allbooking'),
    path('ologout/',views.ologout,name='ologout'),
    path('addroom/',views.addroom,name='addroom'),
    path('facilities/<int:prpid>/',views.facilities,name='facilities'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)