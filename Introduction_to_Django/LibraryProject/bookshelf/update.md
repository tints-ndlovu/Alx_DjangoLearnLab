
---

### **update.md**
```markdown
# Update Operation

```python
from bookshelf.models import Book

# Update the book title
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
book.title
# 'Nineteen Eighty-Four'
