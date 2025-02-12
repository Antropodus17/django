from django.db import models

# Create your models here.


class Blogs(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/blog", blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200, blank=True)
