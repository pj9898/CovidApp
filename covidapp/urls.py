from django.contrib import admin
from django.urls import path
#from .views import helloworldview
from .views import CovidStats
urlpatterns = [
   #path('helloworld/',helloworldview),
    path('',CovidStats),


]
