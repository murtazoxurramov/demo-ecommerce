from django.db import models
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='child', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_category'
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    prize = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='uploads/product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_image'
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.title


class ProductDiscount(models.Model):
    discount_percent = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_discount'
        verbose_name = 'Product Discount'
        verbose_name_plural = 'Product Discounts'

    def save(self, *args, **kwargs):
        discount = (int(self.product.prize) / 100) * self.discount_percent
        result = int(self.product.prize) - int(discount)
        changed_prize = Product.objects.filter(
            id=self.product.pk).get(id=self.product.pk)
        changed_prize.prize = result
        changed_prize.save()
        super(ProductDiscount, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.title
