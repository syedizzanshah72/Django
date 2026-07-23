from django.shortcuts import render,HttpResponse
from myapp.models import ChaiVariety,Store
from datetime import datetime
from django.contrib.messages import constants as messages
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

def index(request):
    chais = ChaiVariety.objects.all()
    return render(request , 'index.html',{'chais': chais})

def about(request):
    return render(request , 'about.html')
    # return HttpResponse("This is about page ")

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVariety,pk=chai_id)
    return render(request,"about.html",{'chai':chai})

def services(request):
    return render(request , 'services.html')
    # return HttpResponse("This is services page ")
def contact(request):
   return render(request,'contact.html')

def chai_view_store(request):
    stores = None
    if request.method == "POST":
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varietes = chai_varity)
            print("Stores found ",stores)
 
    else:
            form = ChaiVarietyForm()
    return render(request,'Contact.html',{'stores':stores ,'form' : form})

        
    

# Create your views here.
