from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    # orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True, default=None)

    class Meta:
        model = CustomUser # get_user_model() #
        fields = ('id', 'email', 'first_name','last_name', 'middle_name','password')
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