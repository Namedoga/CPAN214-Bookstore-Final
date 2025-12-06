from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.author}"
