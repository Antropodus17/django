from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect


from .models import *

# Create your views here.


# def home(request):
#     return render(request, "apps/objects/home.html")


class HomeView(View):
    def get(self, request):
        return render(request, "apps/objects/home.html")

    def post(self, request):
        return render(request, "apps/objects/home.html")


class ObjectsList(ListView):
    template_name = "apps/objects/objects_list.html"
    model = Resource
    context_object_name = "resources"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        markers = getMarkers(self.request)
        context["markers"] = markers
        return context


class DetailsView(DetailView):
    template_name = "apps/objects/objects_details.html"
    model = Resource
    context_object_name = "resource"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        markers = getMarkers(self.request)
        id = self.get_object().id

        if id in markers:
            marked = True
        else:
            marked = False
        context["marked"] = marked
        return context


class ProcessMarker(View):
    def post(self, request):
        id = int(request.POST["id"])
        print(id)
        markers = getMarkers(request)
        if id in markers:
            markers.remove(id)
        else:
            markers.append(id)
        # PRINT THE LIST OF IDS MARKEDS
        print(markers)
        request.session["markers_resources"] = markers
        return HttpResponseRedirect(request.META["HTTP_REFERER"])


class RecipeView(View):
    def get(self, request, pk):
        resource = Resource.objects.get(id=pk)
        recipes = resource.as_crafted_resource.all()
        context = {
            "resource": resource,
            "recipes": recipes,
            "messure": resource.Messure._member_names_,
        }
        # print(resource.Messure._member_names_[0])
        return render(request, "apps/objects/recipes.html", context)
        # return HttpResponseRedirect(request.META["HTTP_REFERER"])


# THIS METHOD IS USED TO BE SURE THAT MARKERS IS INITIALIZATED
def getMarkers(request):
    markers = request.session.get("markers_resources")
    if type(markers) == type(None):
        markers = []
    integer_markers = []
    for mark in markers:
        integer_markers.append(int(mark))
    return integer_markers
