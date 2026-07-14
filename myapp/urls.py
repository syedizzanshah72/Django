from django.contrib import admin
from django.urls import path
from myapp import views 
admin.site.site_header = "Izzan Ice Cream Admin"
admin.site.site_title = "Izzan Admin Portal"
admin.site.index_title = "Welcome to Izzan Researcher Portal"
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),


]
