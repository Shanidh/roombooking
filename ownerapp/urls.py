from django.urls import path, include
from.import views

urlpatterns = [

    path('ologin',views.newfunction,name='ologin'),
    path('osignup',views.newfunction1,name='osignup'),
    path('oprofile',views.newfunction2,name='oprofile'),
    path('oaddroom',views.newfunction3,name='oaddroom'),
    path('list',views.newfunction4,name='list'),
    path('addhotel',views.newfunction5,name='addhotel'),
]