from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request): #accepts a request and returns 
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The City That Never Sleeps"
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Indonesia"
    dest2.desc = "Bhinneka Tunggal Ika"
    dest2.price = 578

    dest3 = Destination()
    dest3.name = "San Francisco"
    dest3.desc = "The City that Knows How"
    dest3.price = 679

    return render(request, 'index.html', {'dest1': dest1, 'dest2': dest2, 'dest3': dest3})
