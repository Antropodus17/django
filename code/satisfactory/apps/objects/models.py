from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators


# from apps.calculator.models
# Create your models here.


class Resource(models.Model):
    class Messure(models.IntegerChoices):
        UDS = 0, _("Units")
        LTR = 1, _("Liters")

    name = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
        validators=[validators.MinLengthValidator(3)],
    )
    img = models.ImageField(upload_to="resources")
    messure = models.IntegerField(default=Messure.UDS, choices=Messure.choices)

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    id_craft_resource = models.ForeignKey(
        Resource, related_name="as_crafted_resource", on_delete=models.CASCADE
    )
    id_needed_resource = models.ForeignKey(
        Resource, related_name="as_needed_resource", on_delete=models.CASCADE
    )
    cuantity = models.FloatField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(999),
        ]
    )

    def __str__(self):
        return f"{self.id_craft_resource.name} recipe"
