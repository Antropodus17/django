from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by("date")[:3]
    return render(request, "index_post.html", {"posts": posts})


def details(request, slug):
    # post = get_object_or_404(Post, {"slug": slug})
    post = Post.objects.get(slug=slug)
    return render(request, "details_post.html", {"post": post})
