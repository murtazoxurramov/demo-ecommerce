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
