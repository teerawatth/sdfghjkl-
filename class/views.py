from django.shortcuts import render
from .models import *

def home(request):
    subject = Subject.objects.all()
    return render(request,'class/home.html',{'subject':subject})
