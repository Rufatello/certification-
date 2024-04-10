from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'password', 'city', 'country', 'street', 'house_number', 'email')
