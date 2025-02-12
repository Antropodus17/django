from django.contrib import admin
from .models import Generator, Recipe, Resource

# Register your models here.

admin.site.register(Generator)
admin.site.register(Recipe)
admin.site.register(Resource)
