from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']
        widget = {
            'username':forms.TextInput(attrs={'class':'input-control'}),
            'email':forms.EmailInput(attrs={'class':'input-control'}),
            'password1':forms.PasswordInput(attrs={'class':'input-control'}),
            'password2':forms.PasswordInput(attrs={'class':'input-control'}),
        }
        
