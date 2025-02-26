from django.contrib import admin
from .models import Generator

# Register your models here.


class GeneratorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Generator, GeneratorAdmin)
