from django.shortcuts import render, get_object_or_404  # type: ignore
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect


from .forms import CommentModelForm
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


class Details(View):
    # template_name = "details_post.html"
    # model = Post

    # def get_context_data(self, **kwargs) -> dict[str, any]:
    #     context = super().get_context_data(**kwargs)
    #     context["tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentModelForm
    #     return context

    def get(self, request, slug):
        # post = get_object_or_ 404(Post, {"slug": slug})
        post = Post.objects.get(slug=slug)
        return render(
            request,
            "details_post.html",
            {
                "post": post,
                "tags": post.tags.all(),
                "comment_form": CommentModelForm(),
                "comments": post.comments.all(),
            },
        )

    def post(self, request, slug):
        form = CommentModelForm(request.POST)
        post = Post.objects.get(slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("details_post", args=[slug]))
        return render(
            request,
            "details_post.html",
            {
                "post": post,
                "tags": post.tags.all(),
                "comment_form": CommentModelForm(),
                "comments": post.comments.all(),
            },
        )


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


class RegisterComment(View):
    pass
