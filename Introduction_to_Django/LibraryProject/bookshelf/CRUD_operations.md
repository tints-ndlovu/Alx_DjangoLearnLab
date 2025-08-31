# CRUD Operations for Book Model

This document demonstrates basic CRUD (Create, Retrieve, Update, Delete) operations using the `Book` model in the `bookshelf` app via the Django shell.

---

## 1. Create

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>

# Retrieve the created book by its ID
book = Book.objects.get(id=1)
book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)

# Update the book title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
book.title
# 'Nineteen Eighty-Four'

# Delete the book instance
book.delete()
# (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# <QuerySet []>
