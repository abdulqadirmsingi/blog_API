from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    # email = models.EmailField(unique=True)
    # username = models.CharField(max_length=30, unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    # def __str__(self):
    #     return self.email


