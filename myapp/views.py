from django.shortcuts import render,HttpResponse
from myapp.models import Contact
from datetime import datetime
from django.contrib.messages import constants as messages

def index(request):

    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')
    # return HttpResponse("This is about page ")

def services(request):
    return render(request , 'services.html')
    # return HttpResponse("This is services page ")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name = name , email = email ,subject = subject , message = message , date = datetime.today())
        contact.save()


    return render(request,'contact.html')
    # return HttpResponse("This is contact page ")


# Create your views here.
