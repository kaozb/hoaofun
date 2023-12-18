from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group


class Userfun(AbstractUser):
    phone = models.CharField("手机号",null=True,blank=True,max_length=1024)
    phone2 = models.CharField("手机号2",null=True,blank=True,max_length=1024)

    def __str__(self):
        return self.username