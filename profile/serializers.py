from rest_framework import serializers

from product.models import Product
from product.serializers import ProductDetailSerializer, ProductListSerializer
from shop.models import Shop
from shop.serializers import ShopDetailSerializer, ShopListSerializer
from users.models import User
from users.serializers import UserDetailSerializer

from .models import VendorProfile


class VendorProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = VendorProfile
        fields = ['user']

    def get_user(self, obj):
        user = User.objects.filter(username=obj)
        if user.exists():
            return UserDetailSerializer(user, many=True).data
        return []


class VendorProfileShopListSerializer(serializers.ModelSerializer):
    shops = serializers.SerializerMethodField()

    class Meta:
        model = VendorProfile
        fields = ['shops']

    def get_shops(self, obj):
        shops = Shop.objects.filter(owner=obj)
        if shops.exists():
            return ShopListSerializer(shops, many=True).data
        return []


class VendorProfileShopSerializer(serializers.ModelSerializer):
    shop = serializers.SerializerMethodField()
    # products = serializers.SerializerMethodField()

    class Meta:
        model = VendorProfile
        fields = ['shop',]

    def get_shop(self, shop_id):
        print("11111111111111111111111111")
        print(shop_id)
        print("11111111111111111111111111")
        shop = Shop.objects.filter(pk=shop_id)
        if shop.exists():
            return ShopDetailSerializer(shop, many=True).data
        return []

    # def get_products(self, obj):
    #     print("!!!!!!!!!!!!!!!!!!!!!!!!")
    #     print(self.get_shop(obj))
    #     print("!!!!!!!!!!!!!!!!!!!!!!!!")
    #     products = Product.objects.filter(shop=self.shop)
    #     if products.exists():
    #         return ProductListSerializer(products, many=True).data
    #     return []
