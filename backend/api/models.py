from django.db import models
import random


class authModel(models.Model):
    username = models.CharField(max_length=22, null=False, unique=True)
    password = models.CharField(max_length=16, null=False)
    mail_id = models.EmailField(max_length=255, null=False, unique=True)
    nickname = models.CharField(max_length=12, null=True)
    bio = models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)




