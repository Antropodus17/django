from django import forms


from apps.objects.models import Recipe, Resource


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["id_needed_resource", "cuantity"]
