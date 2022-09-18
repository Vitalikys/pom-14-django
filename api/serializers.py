from rest_framework import serializers

from author.models import Author
from authentication.models import CustomUser
from book.models import Book
from order.models import Order


class UserSerializer(serializers.ModelSerializer):
    # orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default=None)
    class Meta:
        model = CustomUser  # get_user_model() #
        fields = ('id', 'email', 'first_name', 'last_name', 'middle_name', 'password')
        write_only_fields = ('password')
        # read_only_fields = ('id', 'orders')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'



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

class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        # fields = ('book', 'user', 'created_at', 'end_at', 'plated_end_at')
        fields = '__all__'

