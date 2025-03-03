from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .forms import *


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "apps/forms/recipe_create.html"

    def get_success_url(self):
        print(self.get_object().id_craft_resource.id)
        return reverse_lazy(
            "objects:recipe", args=(self.get_object().id_craft_resource.id,)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resource"] = Resource.objects.get(pk=self.kwargs.get("pk"))
        return context

    def form_valid(self, form):  # DONT ASK DONT TOUCH DONT LOOK, VERY FRAGILE
        form.save(commit=False)
        craft_resource = Resource.objects.get(pk=self.kwargs.get("pk"))

        form.instance.id_craft_resource = craft_resource

        return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "apps/forms/recipe_update.html"

    def get_success_url(self):
        print(self.get_object().id_craft_resource.id)
        return reverse_lazy(
            "objects:recipe", args=(self.get_object().id_craft_resource.id,)
        )


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "apps/forms/recipe_delete.html"

    def get_success_url(self):
        print(self.get_object().id_craft_resource.id)
        return reverse_lazy(
            "objects:recipe", args=(self.get_object().id_craft_resource.id,)
        )
