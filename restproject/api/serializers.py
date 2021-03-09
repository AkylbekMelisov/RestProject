from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'year']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'date_birth', 'date_death', 'bio', 'country', 'books']


class OrderSerializer(serializers.ModelSerializer):
    #book = serializers.PrimaryKeyRelatedField(required=True)
    status = serializers.CharField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'date_create', 'address', 'status', 'quantity']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = Branch
        fields = ['name', 'contacts']