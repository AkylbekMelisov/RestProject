from .models import Comment
from api.models import Book
from rest_framework.serializers import ModelSerializer


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BookDetailSerializer(ModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'year', 'author', 'comment_set']
