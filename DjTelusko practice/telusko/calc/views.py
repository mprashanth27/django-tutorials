from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request): #accepts a request and returns 
    return render(request, 'home.html', {'name':'User'})
