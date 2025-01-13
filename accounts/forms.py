from django import forms
from django.contrib.auth.forms import UserCreationForm

from ckeditor.widgets import CKEditorWidget

from .models import CustomUser

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widget = {
            'username':forms.TextInput(attrs={'class':'input-control'}),
            'email':forms.EmailInput(attrs={'class':'input-control'}),
            'password1':forms.PasswordInput(attrs={'class':'input-control'}),
            'password2':forms.PasswordInput(attrs={'class':'input-control'}),
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture', 'location']
        
    bio = forms.CharField(widget=CKEditorWidget(), required=True)
