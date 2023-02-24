from rest_framework import serializers

from product.models import Product
from product.serializers import ProductDetailSerializer, ProductListSerializer

from .models import Category, Shop


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'child']

    def get_child(self, obj):
        sub_category = Category.objects.filter(parent=obj)
        if sub_category.exists():
            return SubCategorySerializer(sub_category, many=True).data
        return []


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'logo', 'ordinal_number']


class ShopDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = [
            'id', 'name', 'ordinal_number', 'logo', 'latitude', 'longitude', 'category', 'owner', 'address', 'bio', 'products'
        ]

    def get_products(self, obj):
        product = Product.objects.filter(shop=obj)
        return ProductListSerializer(product, many=True).data
