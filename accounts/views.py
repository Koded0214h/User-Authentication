from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.html import strip_tags
from django.template import Library
from django.utils.safestring import mark_safe

from .forms import RegisterForm, ProfileForm
from .models import CustomUser

# Create your views here.

lib = Library()

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

@lib.filter(name='render_bio')
def render_bio(value):
    """
    This filter will render the bio content safely and preserve the HTML formatting.
    """
    return value  # We return the content as is to allow HTML rendering in the template


def profile_view(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    user_profile.bio = mark_safe(user_profile.bio)
    return render(request, 'profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        print('C')
        form = ProfileForm(request.POST, request.FILES, instance=user)
        print('A')
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile', username=user.username)
        else:
            messages.error(request, 'There was an error updating your profile.')
    else:
        print('B')
        form = ProfileForm(instance=user)
        
    user.bio = mark_safe(user.bio)
    return render(request, 'edit_profile.html', {'form': form})

