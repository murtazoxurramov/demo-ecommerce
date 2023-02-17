from django.contrib import admin

from .models import Product, ProductCategory, ProductImage, ProductDiscount

admin.site.register(ProductCategory)
admin.site.register(ProductDiscount)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


# class ProductDiscountAdmin(admin.StackedInline):
#     model = ProductDiscount


@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product
