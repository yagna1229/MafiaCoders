from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name="home"),
   path('event/',views.events,name="events"),
   path('Contact/',views.contact,name="contact"),
   path('aboutus/',views.aboutus,name="aboutus"),
   path('login/',views.loginpage,name="login"),
   path('register/',views.registerPage,name="register"),
   path('logout/',views.logoutPage,name='logout'),
   path('createNewEvent/',views.createEvent,name='creatEvent'),

]
