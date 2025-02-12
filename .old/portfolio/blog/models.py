from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title}"
