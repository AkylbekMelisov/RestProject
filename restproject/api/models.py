from django.contrib.auth.models import User
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


class Order(models.Model):
    statuses = (
        ('pending', 'pending'),
        ('finished', 'finished')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    status = models.CharField(choices=statuses, max_length=20, default='pending')


    def __str__(self):
        try:
            return f"Заказ с товаром: {self.book.title}"
        except AttributeError:
            return "Книга не найдена"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

class Branch(models.Model):
    name = models.CharField(max_length=40)

class Contact(models.Model):
    types = (
        ('email', 'email'),
        ('phone', 'phone'),
        ('address', 'address')
    )
    info = models.CharField(choices=types, max_length=40, default='phone')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='contacts')
