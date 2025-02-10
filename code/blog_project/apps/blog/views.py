from django.shortcuts import render, get_object_or_404  # type: ignore
from django.views import View

from .models import *

# Create your views here.


class Home(View):
    def get(self, request):
        posts = Post.objects.all().order_by("date")[:3]
        return render(request, "index_post.html", {"posts": posts})


class Details(View):
    def get(self, request, slug):
        # post = get_object_or_ 404(Post, {"slug": slug})
        post = Post.objects.get(slug=slug)
        return render(
            request, "details_post.html", {"post": post, "tags": post.tags.all()}
        )


class AllBlogs(View):
    def get(self, request):
        posts = Post.objects.all().order_by("date")
        return render(request, "all_blogs.html", {"posts": posts})
