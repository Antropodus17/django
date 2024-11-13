from django.db import models

# Create your models here.


class Project(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="img")
    url = models.URLField(max_length=200, blank=True)
