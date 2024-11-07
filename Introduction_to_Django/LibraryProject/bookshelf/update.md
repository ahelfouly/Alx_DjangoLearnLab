from bookshelf.models import Book

# Retrieve the book object
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated book object
book
