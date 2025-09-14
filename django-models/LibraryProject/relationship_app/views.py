from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # 👈 same fix here
    context_object_name = "library"


