from django.db import models
from django.contrib.auth.models import User

class BookManager(models.Manager):
    def get_all_books(self):
        return super().get_queryset()

    def get_book_by_id(self, id):
        return self.get(id=id)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.FloatField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # who added the book

    objects = BookManager()

    def __str__(self):
        return f"{self.title} by {self.author}"
