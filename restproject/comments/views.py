from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from api.models import Book
from .models import Comment
from rest_framework.views import APIView
from .serializers import BookDetailSerializer, CommentSerializer


# Create your views here.

class BookDetailView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(id=kwargs['book_id'])
        except Book.DoesNotExist:
            return Response({"data": "NotFound"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "comment create succesfully!"})
        return Response(serializer.errors)

