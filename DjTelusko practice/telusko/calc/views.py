from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(reuest): #accepts a request and returns 
    return HttpResponse("<h1>Hello World</h1>")
