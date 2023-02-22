from rest_framework import serializers

from .models import VendorProfile
from product.models import Product
from users.models import User
from shop.models import Shop

from shop.serializers import ShopDetailSerializer, ShopListSerializer
from users.serializers import UserDetailSerializer
from product.serializers import ProductDetailSerializer, ProductListSerializer


class VendorProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    # shops = serializers.SerializerMethodField()

    class Meta:
        model = VendorProfile
        fields = '__all__'

    def get_user(self, obj):
        user = User.objects.filter(username=obj)
        if user.exists():
            return UserDetailSerializer(user, many=True).data
        return []


class VendorShopListSerializer(serializers.ModelSerializer):
    shops = serializers.SerializerMethodField()

    class Meta:
        model = VendorProfile
        fields = ['id', 'shops']

    def get_shops(self, obj):
        shops = Shop.objects.filter(owner=obj)
        if shops.exists():
            return ShopListSerializer(shops, many=True).data
        return []


class VendorShopDetailSerializer(serializers.ModelSerializer):
    shop = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    class Meta:
        model = VendorProfile
        fields = ['id', 'shop', 'products']

    def get_shop(self, obj):
        shop = Shop.objects.filter(owner=obj)
        if shop.exists():
            return ShopDetailSerializer(shop, many=True).data
        return []

    def get_products(self, obj):
        shop = Shop.objects.filter(owner=obj)
        product = Product.objects.filter(shop=shop)
        return ProductListSerializer(product, many=True).data
