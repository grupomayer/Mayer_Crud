from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
class Nome(AbstractUser):
    nome = models.CharField(max_length=255)
class Cpf(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
class Email(AbstractUser):
    email = models.EmailField(max_length=255)
