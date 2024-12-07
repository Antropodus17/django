from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "project/index.html")


def aplication(request):
    return render(request, "apps/courses/index.html")
