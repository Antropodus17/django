from django.db import models


from apps.objects.models import Resource

# Create your models here.


class Generator(models.Model):
    name = models.CharField(max_length=50, unique=True)
    power = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"
