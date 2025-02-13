from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.code}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.street} - {self.postal_code} - {self.city}"

    class Meta:
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):

        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    raiting = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="fkbooks"
    )
    is_bestsealing = models.BooleanField(default=False)
    slug = models.SlugField(
        default="",
        null=False,
        db_index=True,
        blank=True,
    )
    published_countries = models.ManyToManyField(Country, verbose_name="fkcountries")

    def __str__(self):
        return f"{self.id}-{self.title} ({self.raiting})"

    def get_absolute_url(self):
        return reverse("book:details", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
