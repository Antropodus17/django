from django.db import models

# Create your models here.


class userLogin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    webServer = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    payroll = models.CharField(max_length=255)
    selfServices = models.CharField(max_length=255)
