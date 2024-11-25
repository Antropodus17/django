from django.db import models

# Create your models here.


class Generator(models.Model):
    name = models.CharField(max_length=50)
    powerGenerated = models.IntegerField()
    img = models.ImageField(upload_to="img/calculator")

    def calcuateEnergySuply(self, rendimiento=1):
        return self.powerGenerated * rendimiento


class Resource(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/calculator/resources")
    basic = models.BooleanField()


class Recipe(models.Model):
    resultado = models.ForeignKey(
        Resource,
        related_name="Resultado",
        on_delete=models.CASCADE,
    )
    uds = models.SmallIntegerField()
    primaryResource1 = models.ForeignKey(
        Resource,
        related_name="Material_1",
        on_delete=models.CASCADE,
    )
    primaryResource2 = models.ForeignKey(
        Resource,
        related_name="Material_2",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    primaryResource3 = models.ForeignKey(
        Resource,
        related_name="Material_3",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    primaryResource4 = models.ForeignKey(
        Resource,
        related_name="Material_4",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    udsResource1 = models.SmallIntegerField()
    udsResource2 = models.SmallIntegerField(blank=True, null=True)
    udsResource3 = models.SmallIntegerField(blank=True, null=True)
    udsResource4 = models.SmallIntegerField(blank=True, null=True)
    ticks = models.SmallIntegerField()
