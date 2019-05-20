from django.shortcuts import render
from .models import Myapp

# Create your views here.
def home(request):
    myapp = Myapp.objects
    return render(request,'home.html',{'Myapp':myapp}) 