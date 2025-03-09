from django.contrib import admin
from .models import Resource
from .models import Recipe

# Register your models here.


class ResourceAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = (
        "name",
        "messure",
    )


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["craft_name"]
    list_filter = (
        "id",
        "id_craft_resource",
    )

    @admin.display(ordering="resource__name")
    def craft_name(self, obj: Recipe):
        return obj.id_craft_resource.name


admin.site.register(Resource, ResourceAdmin)
admin.site.register(Recipe, RecipeAdmin)
