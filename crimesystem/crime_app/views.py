from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request, "users/dashboard.html")

def casesview(request):
    context ={}
 
    # create object of form
    form = casesform(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, "users/dashboard.html", context)