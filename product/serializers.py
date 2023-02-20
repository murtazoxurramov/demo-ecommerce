from rest_framework import serializers

from .models import Product, ProductDiscount, ProductImage


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
        fields = ['id', 'title', 'price', 'shop', 'discount', 'image']

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
        fields = [
            'id', 'title', 'category', 'price',
            'shop', 'discount', 'description', 'images'
        ]

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
