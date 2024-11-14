from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    return render(
        request,
        "index-portfolio.html",
        context={"projects": Project.objects.all()},
    )
