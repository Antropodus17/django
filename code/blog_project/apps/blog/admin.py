from django.contrib import admin
from .models import Tag
from .models import Author
from .models import Post

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author")
    list_filter = ("author", "tags", "date")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
