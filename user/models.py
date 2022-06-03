from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.CharField("user address", max_length=100, blank=True, null=True)
    phone = models.CharField("user phone", max_length=20, blank=True, null=True)
