from django.shortcuts import render , redirect ,HttpResponseRedirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import register
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = authenticate(request , username = User.objects.get(email=username) , password = password)
            except:
                user = authenticate(request , username = username ,password = password)
            if user is not None:
                login(request , user)
                messages.add_message(request, messages.SUCCESS , (f"{username} loged in successfuly ."), {'username':username}) 
                return redirect('/')
            else:
                messages.error(request,'username or password not correct')
                return HttpResponseRedirect(reverse('accounts:login'))
        form = AuthenticationForm()
        context = {'form': form}
        return render(request , 'accounts/login.html' , context)
    elif request.user.is_authenticated:
        return redirect('/')



@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = register(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('accounts:login'))
            else:  # if the form is not valid, pass the invalid form in the context
                return render(request,'accounts/signup.html', { 'form' : form, })
        form = register()
        context = {'form': form}
        return render(request , 'accounts/signup.html' , context)
    else:
        return redirect('/')
