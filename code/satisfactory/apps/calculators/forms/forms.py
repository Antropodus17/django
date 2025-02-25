from django import forms

from apps.calculators.models import Recipe


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
