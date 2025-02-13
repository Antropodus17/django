from django.contrib import admin
from .models import Review
from .models import NovellServiceModel

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    pass

class NovellServiceModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, ReviewAdmin)
admin.site.register(NovellServiceModel, NovellServiceModelAdmin)
