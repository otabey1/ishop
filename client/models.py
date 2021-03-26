from django.db import models
# from main import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField()
