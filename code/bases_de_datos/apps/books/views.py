from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, "index_book.html", {"books": books})


def details(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(
        request,
        "details_book.html",
        {
            "title": book.title,
            "author": book.author,
            "is_bestsealing": book.is_bestsealing,
        },
    )
