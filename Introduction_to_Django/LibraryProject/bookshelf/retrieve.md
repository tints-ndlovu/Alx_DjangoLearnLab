
---

### **retrieve.md**
```markdown
# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the created book by its ID
book = Book.objects.get(id=1)
book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)
