from django.forms import forms

from apps.objects.models import Resource


class ResourceForm(forms.Modelform):
    class Meta:
        model = Resource
        fields = "__all__"
