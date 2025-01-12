from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):

    # Other Fields 
    profile_picture = models.ImageField(upload_to='profile_picture/')
    
    def __str__(self):
        return self.username
