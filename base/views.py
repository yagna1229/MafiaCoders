from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import EventForm

# Create your views here.

def home(request):
    return render(request,'base/home.html')

def events(request):
    return render(request,'base/events.html')

def contact(request):
    return render(request,'base/contact.html')

def aboutus(request):
    return render(request,'base/aboutus.html')


def loginpage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username= username)
            
        except:
            messages.error(request,"User does not exits")

        user = authenticate(request,username=username,password= password)


        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Error in login- Username - password does not exits")
    context ={'page':page}

    return render(request,"base/loginRegister.html",context)

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request,user)
        return redirect('home')
    else:
        messages.error(request,"Error during registation occured")
    return render(request,"base/loginRegister.html",{'form':form})

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def createEvent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    context = {
        'form':form
    }
    return render(request,"base/createEvent.html",context)
