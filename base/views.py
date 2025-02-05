from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'base/home.html')

def events(request):
    return render(request,'base/events.html')

def contact(request):
    return render(request,'base/contact.html')

def aboutus(request):
    return render(request,'base/aboutus.html')