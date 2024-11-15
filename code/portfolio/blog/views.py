from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def all_blogs(request):

    return render(
        request,
        "index-blog.html",
        context={"blogs": Blog.objects.all().order_by("fecha")[:2]},
    )


def detail(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, "details-blog.html", {"blog": blog})
