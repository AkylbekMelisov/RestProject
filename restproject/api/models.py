from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    year = models.DateField()
    book_file = models.FileField(blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    date_birth = models.DateField()
    date_death = models.DateField(blank=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name