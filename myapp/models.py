from django.db import models
from django.contrib.auth.models import AbstractUser  
from .manager import UserManager
# Create your models here.
class Sign(AbstractUser):
    username=models.CharField(max_length=100,unique=True)
    mobile=models.CharField(max_length=10,unique=True)
    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]


