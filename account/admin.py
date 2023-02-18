from django.contrib import admin

from .models import OrdinaryUser, Shop, ShopCategory, Vendor

# @admin.register(OrdinaryUser)
# class OrdinaryUserAdmin(admin.ModelAdmin):

admin.site.register(OrdinaryUser)
admin.site.register(Vendor)
admin.site.register(ShopCategory)
admin.site.register(Shop)
