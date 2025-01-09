from django.db import models

# Create your models here.


class Hola(models.Model):
    a = models.IntegerField()


class Mundo(models.Model):
    b = models.TextField()
