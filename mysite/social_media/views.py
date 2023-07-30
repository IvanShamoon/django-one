from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def starting_point(request):
    return render(request, 'social_media/base.html')

def home_page(request):
    return render(request, 'social_media/home_page.html')

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/sign_up.html', {"form":form})