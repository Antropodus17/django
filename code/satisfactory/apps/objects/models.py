from django.db import models
from django.utils.translation import gettext_lazy as _

# from apps.calculator.models
# Create your models here.


class Resource(models.Model):
    class Messure(models.IntegerChoices):
        UDS = 0, _("Units")
        LTR = 1, _("Liters")

    name = models.CharField(max_length=50, unique=True)
    img = models.ImageField(upload_to="resources")
    messure = models.IntegerField(default=Messure.UDS, choices=Messure.choices)

    def __str__(self):
        return f"{self.name}"
