from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # 👈 same fix here
    context_object_name = "library"

# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        # Use CustomUserCreationForm if role is included
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")
            if role:  # only update if role was selected
                user.userprofile.role = role
                user.userprofile.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")  # can point to any landing page
    else:
        form = CustomUserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


# Helper functions for role checks
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# Views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

from django.shortcuts import  redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# Add book (requires can_add_book)
@permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        author = Author.objects.get(id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect("list_books")
    authors = Author.objects.all()
    return render(request, "relationship_app/add_book.html", {"authors": authors})


# Edit book (requires can_change_book)
@permission_required("relationship_app.can_change_book")
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        author_id = request.POST.get("author")
        book.author = Author.objects.get(id=author_id)
        book.save()
        return redirect("list_books")
    authors = Author.objects.all()
    return render(request, "relationship_app/edit_book.html", {"book": book, "authors": authors})


# Delete book (requires can_delete_book)
@permission_required("relationship_app.can_delete_book")
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
