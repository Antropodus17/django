from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect


class ResourceCreateView(CreateView):
    pass


class ResourceDeleteView(DeleteView):
    pass


class ResourceUpdateView(UpdateView):
    pass
