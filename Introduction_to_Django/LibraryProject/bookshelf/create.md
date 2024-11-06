# CRUD Operations for Book Model

This file documents the CRUD operations performed on the `Book` model in the `bookshelf` app.

### 1. Create Operation

```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Display the created book object
book
