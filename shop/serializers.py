from rest_framework import serializers

from profile.models import VendorProfile
from .models import Shop, ShopCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = ['id', 'title', 'slug']


# class CategoryLogoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MainPageSettings
#         fields = ['logo_url']


class ShopCategorySerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()

    class Meta:
        model = ShopCategory
        fields = ['id', 'title', 'slug', 'child']

    def get_child(self, obj):
        sub_category = ShopCategory.objects.filter(parent=obj)
        if sub_category.exists():
            return SubCategorySerializer(sub_category, many=True).data
        return []


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'logo', 'ordinal_number']


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'id', 'name', 'ordinal_number', 'logo', 'latitude', 'longitude', 'category', 'owner', 'address', 'bio'
        ]


class VendorShopSerializer(serializers.ModelSerializer):
    vendor = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'logo', 'ordinal_number', 'vendor']

    def get_vendor(self, obj):
        vendor = Shop.objects.filter(owner=obj)
