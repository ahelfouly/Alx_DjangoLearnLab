from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    
    class Meta:
    permissions = [
        ('can_add_book', 'Can add book'),           
        ('can_change_book', 'Can change book'),      
        ('can_delete_book', 'Can delete book'), 
        ]

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Author, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    class Roles(models.TextChoices):
        admin = "Admin"
        librarian = "Librarian"
        member = "Member"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofiles')
    role = models.CharField(max_length=20, choices=Roles, default=Roles.member)

    def __str__(self):
        return f"{self.user.username}'s profile."