from rest_framework import serializers

# from author.models import Author
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=128)
    # description = serializers.CharField(max_length=256)
    # count = serializers.IntegerField(default=10)
    # # id = serializers.IntegerField() #primary_key=True)
    # authors = serializers.ManyRelatedField(read_only=True, source='Author')
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'id', 'authors')
      # exclude = поля джанго-модели, для которых не нужно создавать поля
    # def create(self, validated_data):
    #     return Book.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.count = validated_data.get('count', instance.count)
    #     instance.authors = validated_data.get('authors', instance.authors)
    #     instance.save()
    #     return instance
