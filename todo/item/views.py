from django.shortcuts import render
from .models import Item
from django.http import HttpResponse
from django.shortcuts import render 
# Create your views here.

def index(request):
    return HttpResponse('testing 1234 Items')
    
