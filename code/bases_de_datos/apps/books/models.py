from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    raiting = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestsealing = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}-{self.title} ({self.raiting})"
