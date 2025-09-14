from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
books_by_author = Book.objects.filter(author__name="J.K. Rowling")

# 2. List all books in a library
books_in_library = Library.objects.get(name="Central Library").books.all()

# 3. Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library__name="Central Library")
