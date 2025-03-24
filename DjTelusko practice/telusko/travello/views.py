from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #accepts a request and returns 
    return render(request, 'index.html')
