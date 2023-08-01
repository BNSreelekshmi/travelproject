from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # static web page task

    path('',views.demostatic,name='demo')





    # new project task
    # path('',views.funhome,name='home'),
    # path('about/', views.funabout, name='about'),
    # path('details/', views.fundetail, name='details'),
    # path('contact/', views.funcontact, name='contact'),
    # path('thanx/', views.funthanx, name='thanx')

    # passing value task
    # path('', views.funhome, name='home'),
    # path('cal/', views.operations, name='op')
]