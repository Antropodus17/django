from django.shortcuts import render
from .models import Blog

# Create your views here.


def all_blogs(request):

    return render(request, "index-blog.html", context={"blogs": Blog.objects.all()})
