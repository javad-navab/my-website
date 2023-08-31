from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from website.forms import Nameform , ContactForm , newsletterform
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request , 'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            messages.add_message(request, messages.SUCCESS , 'your ticket submited successfully')
            form.save()
        else:
            messages.add_message(request, messages.ERROR , 'Your ticket submission failed')
    form = ContactForm()
    return render(request,'website/contact.html' , {'form': form})


def newsletter(request):
    if request.method == 'POST':
        form = newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def test(request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('error')
    form = ContactForm()
    return render(request , 'website/test.html' , {'form': form})