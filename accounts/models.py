from django.db import models
from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

# Create your models here.

class CustomUser(AbstractUser):

    # Other Fields 
    bio = RichTextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/')
    location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.username
