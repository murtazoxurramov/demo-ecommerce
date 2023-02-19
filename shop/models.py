from django.conf import settings
from django.db import models

from profile.models import VendorProfile


class ShopCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ar = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shop_category'
        verbose_name = 'Shop Category'
        verbose_name_plural = 'Shop Categories'

    def __str__(self):
        return self.title


class Shop(models.Model):
    name = models.CharField(max_length=255)
    ordinal_number = models.IntegerField(blank=True, null=True)
    logo = models.FileField(upload_to='upload/market', blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        VendorProfile, on_delete=models.SET_NULL, related_name='vendor', blank=True, null=True
    )
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shop'
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.name

    @property
    def logo_url(self):
        if self.logo:
            return "%s%s" % (settings.HOST, self.logo.url)

