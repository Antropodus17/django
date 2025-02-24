from django.db import models


from apps.objects.models import Resource

# Create your models here.


class Generator(models.Model):
    name = models.CharField(max_length=50, unique=True)
    power = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    id_craft_resource = models.ForeignKey(
        Resource, related_name="as_crafted_resource", on_delete=models.CASCADE
    )
    id_needed_resource = models.ForeignKey(
        Resource, related_name="as_needed_resource", on_delete=models.CASCADE
    )
    cuantity = models.PositiveIntegerField()
