from rest_framework import serializers
from .models import Product, ProductCategory, ProductDiscount, ProductImage


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'title', 'slug']


class ProductSubCategoryerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = ['id', 'title', 'slug', 'child']

    def get_child(self, obj):
        sub_menu = ProductCategory.objects.filter(parent=obj)
        if sub_menu.exists():
            return ProductSubCategoryerializer(sub_menu, many=True).data
        return []


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']


class ProductDiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDiscount
        fields = ['id', 'name', 'percent_off',
                  'discounted_price', 'start_date', 'end_date']


class ProductMainSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price',
                  'discount', 'image']

    def get_discount(self, obj):
        discount = ProductDiscount.objects.filter(product=obj)
        if discount.exists():
            return ProductDiscountSerializer(discount, many=True).data
        return []

    def get_image(self, obj):
        image = ProductImage.objects.filter(product=obj).filter(is_main=True)
        if image.exists():
            return ProductImageSerializer(image, many=True).data
        return []


class ProductDetailSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'price',
                  'discount', 'description', 'images']

    def get_discount(self, obj):
        discount = ProductDiscount.objects.filter(product=obj)
        if discount.exists():
            return ProductDiscountSerializer(discount, many=True).data
        return []

    def get_images(self, obj):
        images = ProductImage.objects(product=obj)
        if images.count() != 1:
            images = images.filter(is_main=False)
            return ProductImageSerializer(images, many=True).data
        return ProductImageSerializer(images, many=True).data
