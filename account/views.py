from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import  User,auth

from try1.models import Destination
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user_name = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username_taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email_taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matching...')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")



def login(request):
    if request.method=='POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)

            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')



def destination_details(request):
    if request.user.is_authenticated:

        dests = Destination.objects.all()
        return render(request, "destination_details.html",{'dests':dests})
    else:
        return redirect('login')
