from rest_framework import serializers
# from author.models import Author
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
     # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
     class Meta:
        model = Order
        # fields = ('book', 'user', 'created_at', 'end_at', 'plated_end_at')
        fields = '__all__'

