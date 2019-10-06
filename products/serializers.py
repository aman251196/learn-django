from rest_framework import serializers

from .models import Product

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Product

class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'price', 'description')
        model = Product
        