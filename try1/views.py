from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination
# Create your views here.
def index(request):
    dests=Destination.objects.all()
    return render(request, "index.html",{'dests':dests})


def about(request):

    return render(request, "about.html")


def contact(request):

    return render(request, "contact.html")
def travel_destination(request):
    dests = Destination.objects.all()
    return render(request, "travel_destination.html",{'dests':dests})