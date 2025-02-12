from django.shortcuts import render, get_object_or_404  # type: ignore
from django.views import View
from django.views.generic import ListView, DetailView


from .models import *

# Create your views here.


class Home(ListView):
    template_name = "index_post.html"
    model = Post
    fields = "__all__"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all().order_by("date")[:3]

    # def get(self, request):
    # posts = Post.objects.all().order_by("date")[:3]
    # return render(request, "index_post.html", {"posts": posts})


class Details(DetailView):
    template_name = "details_post.html"
    model = Post

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context

    # def get(self, request, slug):
    #     # post = get_object_or_ 404(Post, {"slug": slug})
    #     post = Post.objects.get(slug=slug)
    #     return render(
    #         request, "details_post.html", {"post": post, "tags": post.tags.all()}
    #     )


class AllBlogs(ListView):
    template_name = "all_blogs.html"
    model = Post
    fields = "__all__"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all().order_by("date")

    # def get(self, request):
    #     posts = Post.objects.all().order_by("date")
    #     return render(request, "all_blogs.html", {"posts": posts})
