from django.contrib import admin
from .models import Country
from .models import Address
from .models import Author
from .models import Book

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author")


admin.site.register(Country, CountryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
