from django.contrib import admin

from .models import Product, ProductCategory, ProductDiscount, ProductImage

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductDiscount)
admin.site.register(ProductImage)


# class ProductImageAdmin(admin.StackedInline):
#     model = ProductImage

# @admin.register(ProductImage)
# class ProductImage(admin.ModelAdmin):
#     inlines = [ProductImageAdmin]

#     class Meta:
#         model = Product


# class ProductDiscountAdmin(admin.StackedInline):
#     model = ProductDiscount


# @admin.register(ProductDiscount)
# class ProductDiscount(admin.ModelAdmin):
#     inlines = [ProductDiscountAdmin]

#     class Meta:
#         model = Product

