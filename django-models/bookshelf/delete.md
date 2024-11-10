from bookshelf.models import Book

# Delete the book
book.delete()

# Try to retrieve all books again
Book.objects.all()
