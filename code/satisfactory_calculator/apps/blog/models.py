from django.db import models

# Create your models here.


class Blogs(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="models/blogs/img")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=False)
    url = models.URLField(max_length=200)
