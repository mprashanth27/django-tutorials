from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request): #accepts a request and returns 
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The City That Never Sleeps"
    dest1.price = 700
    return render(request, 'index.html', {'dest1': dest1})
