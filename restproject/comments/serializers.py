from .models import Comment
from api.models import Book
from rest_framework.serializers import ModelSerializer, Serializer, CharField, SerializerMethodField
from estimate.serializers import RateModelSerializer


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BookDetailSerializer(ModelSerializer):
    rates = RateModelSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    avg_rate = SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'year', 'author', 'comment_set', 'rates', 'avg_rate']

    def get_avg_rate(self, obj):
        total_sum = 0
        for rate in obj.rates.all():
            total_sum += rate.star
            avg_rate = total_sum / len(obj.rates.all())
        return avg_rate


class CommentCreateSerializer(Serializer):
    text = CharField(allow_blank=False)
