from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('regis',views.regis,name='regis'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]