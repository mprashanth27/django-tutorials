from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request): #accepts a request and returns 
    return render(request, 'home.html', {'name':'User'})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result':res})