from rest_framework import serializers
from shop.models import Factory, Product, Retail, Entrepreneur
from users.serializers import UserSerializer


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class FactorySerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Factory
        fields = ('name', 'user', 'product' )


class FactorySerializersList(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializers(read_only=True)

    class Meta:
        model = Factory
        fields = ('name', 'user', 'product' )


class RetailSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Retail
        fields = '__all__'


class RetailSerializersList(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializers(read_only=True)
    factory = FactorySerializers(read_only=True)

    class Meta:
        model = Retail
        fields = ('name', 'user', 'product', 'sum', 'factory')


class EntrepreneurSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Entrepreneur
        fields = '__all__'


class EntrepreneurSerializersList(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializers(read_only=True)
    factory = FactorySerializers(read_only=True)
    retail = EntrepreneurSerializers(read_only=True)

    class Meta:
        model = Entrepreneur
        fields = ('name', 'user', 'product', 'sum', 'factory', 'retail',)

