from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Profile


# Create your views here.
def demo(request):
    return render(request,"demo.html")
def  about(request):
    return render(request,"about.html")
def index(request):
    obj=Place.objects.all()
    pro=Profile.objects.all()
    return render(request,"index.html",{'result':obj,'presult':pro})