
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('crowdManagerAdmin/',admin.site.urls),
    path('', include('base.urls')),
]
