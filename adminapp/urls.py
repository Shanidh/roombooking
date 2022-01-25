from django.urls import path, include
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('alogin/',views.adlogin,name='alogin'),
     path('asignup/',views.asignup,name='asignup'),
     path('alogout/',views.alogout,name='alogout'),
     path('admindashboard',views.admindb,name='admindashboard'),
     path('viewproperty/<int:propvid>/',views.adminviewppt,name='viewproperty'),
     path('ownerss',views.ownerss,name='ownerss'),
     path('editowners',views.editowners,name='editowners'),
     path('addowners',views.addowners,name='addowners'),
     path('customers',views.customers,name='customers'),
     path('settings/',views.settings,name='settings'),
     path('booking',views.booking,name='booking'),
     path('ablogs',views.ablogs,name='ablogs'),
     path('editblog/<int:blid>/',views.editblog,name='editblog'),
     path('feedbacks',views.feedbacks,name='feedbacks'),
     path('upadmin',views.upadmin,name='upadmin'),
     path('changepass',views.changepass,name='changepass'),
     path('upimage',views.upimage,name='upimage'),
     path('deleteprop/<int:propid>/',views.deleteprop,name='deleteprop'),
     path('deleteown/<int:ownid>/',views.deleteown,name='deleteown'),
     path('addowner',views.addowner,name='addowner'),
     path('deletecust/<int:custid>/',views.deletecust,name='deletecust'),
     path('delofb/<int:ofbid>/',views.delofb,name='delofb'),
     path('delcfb/<int:cfbid>/',views.delcfb,name='delcfb'),
     path('addblog',views.addblog,name='addblog'),
     path('addedblog',views.addedblog,name='addedblog'),
     path('editedblog',views.editedblog,name='editedblog'),
     path('delblog/<int:delbid>/',views.delblog,name='delblog'),
     path('delbk/<int:delbkid>/',views.delbk,name='delbk'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)