from django.contrib import admin
from .models import Generator
from .models import Recipe

# Register your models here.

class GeneratorAdmin(admin.ModelAdmin):
    pass

class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Generator, GeneratorAdmin)
admin.site.register(Recipe, RecipeAdmin)
