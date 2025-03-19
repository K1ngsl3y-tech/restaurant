from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from restapp.models import *


# Create your views here.
def index(request):
    return render(request,'index.html')
def starterpage(request):
    return render(request,'starterpage.html')

def contact(request):
    return render(request,'contact.html')

def events(request):
    return render(request,'events.html')

def about(request):
    return render(request,'about.html')

def specials(request):
    return render(request,'specials.html')

def chefs(request):
    return render(request,'chefs.html')

def menu(request):
    return render(request,'menu.html')

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/index')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')

def table1(request):
    if request.method == "POST":
        mytables = table(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            people = request.POST['people'],
            time = request.POST['time'],
            message = request.POST['message'],
        )
        mytables.save()
        return redirect('/show')

    else:
        return render(request,'table.html')



def contact1(request):
    if request.method == "POST":
        mycontacts = contact(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            number = request.POST['number'],
            time = request.POST['time'],
            message = request.POST['message'],
        )
        mycontacts.save()
        return redirect('/show')

    else:
        return render(request,'contact.html')


def show(request):
    all = table.objects.all()
    return render(request,'show.html',{'all':all})


