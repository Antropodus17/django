from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
