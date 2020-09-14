from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name ='index'),
path('about',views.about,name ='about'),
path('contact',views.contact,name ='contact'),
path('travel_destination',views.travel_destination,name ='travel_destination'),
#path('destination_details',views.destination_details,name ='destination_details'),
]
