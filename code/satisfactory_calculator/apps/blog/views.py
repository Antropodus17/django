from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.


def home(request):
    blogs = Blogs.objects.all()
    return render(request, "blog_index.html", {"blogs": blogs})


def details(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, "blog_details.html", {"blog": blog})
