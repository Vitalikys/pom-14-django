from rest_framework import serializers
from author.models import Author
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'id', 'authors')
        # exclude = поля джанго-модели, для которых не нужно создавать поля
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True) #primary_key=True)
#     name = serializers.CharField(max_length=128, allow_blank=True,  required=False)
#     description = serializers.CharField(max_length=256, allow_blank=True)
#     count = serializers.IntegerField(default=10,  required=False)
#     authors = serializers.PrimaryKeyRelatedField(many=True,label='Автор', queryset=Author.objects.all(), required=False)#, source='Author')
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.count = validated_data.get('count', instance.count)
#         instance.authors = validated_data.get('authors', instance.authors)
#         instance.save()
#         return instance
