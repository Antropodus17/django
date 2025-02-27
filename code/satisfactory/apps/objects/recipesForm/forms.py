from django import forms
from django.db.models import Q


from apps.objects.models import Recipe, Resource


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["id_needed_resource", "cuantity"]
