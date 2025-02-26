from django.contrib import admin
from .models import Resource
from .models import Recipe

# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
    pass

class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Recipe, RecipeAdmin)
