from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register,name ='register'),
    path('login', views.login,name ='login'),
    path('logout',views.logout,name ='logout'),
    path('destination_details',views.destination_details,name ='destination_details'),
    ]
