import django
from django.conf import settings
from relationship_app.models import Author, Book, Library, Librarian

# Set up Django settings if running this script standalone
settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'relationship_app',
    ],
)
django.setup()

# Query 1: Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Accessing the related books using reverse relationship
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

# Query 2: List all books in a library
def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Accessing the related books
        print(f"Books in the {library.name} library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

# Query 3: Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Accessing the related librarian
        print(f"The librarian for the {library.name} library is {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")

# Test Queries
if __name__ == "__main__":
    # Test: Query all books by a specific author
    query_books_by_author("J.K. Rowling")

    # Test: List all books in a specific library
    query_books_in_library("Central Library")

    # Test: Retrieve the librarian for a specific library
    query_librarian_for_library("Central Library")