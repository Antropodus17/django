from django.db import models

# Create your models here.


class Generator(models.Model):
    name = models.CharField(max_length=50)
    powerGenerated = models.IntegerField()

    def calcuateEnergySuply(self, rendimiento=1):
        return self.powerGenerated * rendimiento
