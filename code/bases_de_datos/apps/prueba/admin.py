from django.contrib import admin
from .models import Hola
from .models import Adios
from .models import PruebaHecha

# Register your models here.

class HolaAdmin(admin.ModelAdmin):
    pass

class AdiosAdmin(admin.ModelAdmin):
    pass

class PruebaHechaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hola, HolaAdmin)
admin.site.register(Adios, AdiosAdmin)
admin.site.register(PruebaHecha, PruebaHechaAdmin)
