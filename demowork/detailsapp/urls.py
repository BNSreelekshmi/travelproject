from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static

from demowork import settings

urlpatterns = [
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]
