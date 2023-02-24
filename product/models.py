from django.conf import settings
from django.db import models
from django.utils import timezone

from shop.models import Category, Shop


class Product(models.Model):
    title = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        category_pk = self.shop.category
        # category = Category.objects.filter(pk=category_pk)
        self.category = category_pk
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='uploads/product')
    is_main = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_image'
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.title

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)


class ProductDiscount(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    percent_off = models.DecimalField(max_digits=5, decimal_places=2)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_discount'
        verbose_name = 'Product Discount'
        verbose_name_plural = 'Product Discounts'

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        if self.is_active():
            return self.apply_discount(self.product.price)
        else:
            ProductDiscount.objects.filter(id=self.pk).delete()
            return self.product.price

    def is_active(self):
        now = timezone.now()
        return self.start_date <= now and self.end_date >= now

    def apply_discount(self, price):
        return price * (1 - self.percent_off / 100)
