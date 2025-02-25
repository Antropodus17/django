from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect

from .forms import *


class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = "apps/forms/create.html"
    success_url = "/list"


class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = "apps/forms/delete.html"
    success_url = "/list"


class ResourceUpdateView(UpdateView):
    model = Resource
    form_class = ResourceForm
    template_name = "apps/forms/update.html"
    success_url = "/list"
    template_name_suffix = "update_form"
