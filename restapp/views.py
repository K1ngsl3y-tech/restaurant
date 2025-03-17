from django.shortcuts import render

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
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')





