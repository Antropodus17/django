from django.shortcuts import render

# Create your views here.


def all_blogs(request):
    return render(request, "index.html")
