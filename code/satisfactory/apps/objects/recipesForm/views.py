from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views import View
from django.http import HttpResponseRedirect

from .forms import *


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "apps/forms/recipe_create.html"
    success_url = "/list"

    def form_valid(self, form):  # DONT ASK DONT TOUCH DONT LOOK, VERY FRAGILE
        form.save(commit=False)
        craft_resource = Resource.objects.get(pk=self.kwargs.get("pk"))
        form.instance.id_craft_resource = craft_resource

        return super().form_valid(form)
