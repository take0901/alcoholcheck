from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    catnumber = models.IntegerField(max_length=10)