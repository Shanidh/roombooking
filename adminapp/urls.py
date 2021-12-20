from django.urls import path, include
from.import views

urlpatterns = [
     path('alogin',views.adlogin,name='alogin'),
     path('admindashboard',views.admindb,name='admindashboard'),
     path('editproperty',views.admineditppt,name='editproperty'),
     path('owners',views.owners,name='owners'),
     path('editowners',views.editowners,name='editowners'),
     path('addowners',views.addowners,name='addowners'),
     path('customers',views.customers,name='customers'),
     path('settings',views.settings,name='settings'),
     path('booking',views.booking,name='booking'),
     path('ablogs',views.ablogs,name='ablogs'),
     path('editblog',views.editblog,name='editblog'),
     path('feedbacks',views.feedbacks,name='feedbacks'),
]