from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm
from .models import CustomUser

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid form!')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'registerform':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome back!')
                return redirect('home')
            else:
                messages.error(request, 'User is null!')
        else:
            messages.error(request, 'Invalid form!')
    else:
        form = AuthenticationForm()
    return render(request, 'sign-in.html', {'loginform':form})

def home(request):
    user = request.user
    return render(request, 'home.html', {'user':user})