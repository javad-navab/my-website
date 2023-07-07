from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1> HOME Page </h1>')

def about(request):
    return HttpResponse('<h1> About Page </h1>')

def contact(request):
    return HttpResponse('<h1> contact Page </h1>')
