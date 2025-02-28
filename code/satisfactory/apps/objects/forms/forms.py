from django import forms


from apps.objects.models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"
