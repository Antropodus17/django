from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("raiting", "author")
    list_display = ("title", "author", "raiting")
    # readonly_fields = ["slug"]


admin.site.register(Book, BookAdmin)
