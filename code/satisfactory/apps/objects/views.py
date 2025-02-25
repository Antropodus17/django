from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect


from .models import Resource

# Create your views here.


# def home(request):
#     return render(request, "apps/home.html")


class HomeView(View):
    def get(self, request):
        return render(request, "apps/home.html")

    def post(self, request):
        return render(request, "apps/home.html")


class ObjectsList(ListView):
    template_name = "apps/objects_list.html"
    model = Resource
    context_object_name = "resources"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["markers"] = self.request.session.get("markers_resources")
        return context


class DetailsView(DetailView):
    template_name = "apps/objects_details.html"
    model = Resource
    context_object_name = "resource"


class ProcessMarker(View):
    def post(self, request):
        id = request.POST["id"]
        markers = request.session.get("markers_resources")
        if type(markers) == type(None):
            markers = []
        if id in markers:
            markers.remove(id)
        else:
            markers.append(id)
        print(markers)
        request.session["markers_resources"] = markers
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
