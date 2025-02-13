from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView


from .models import UserProfile

# Create your views here.


class CreateUserProfile(CreateView):
    template_name = "create.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ListProfiles(ListView):
    template_name = "list.html"
    model = UserProfile
    context_object_name = "profiles"
