from django.contrib import admin  # type:ignore
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Review, ReviewAdmin)
